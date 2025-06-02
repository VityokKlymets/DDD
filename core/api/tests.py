from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import User, Order

class UserTests(APITestCase):

    def test_user_registration(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'strongpassword',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_login(self):
        user = User.objects.create_user(username='testuser', password='strongpassword')
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'strongpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

class OrderTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='owner', password='pass')
        self.admin = User.objects.create_user(username='admin', password='adminpass', is_admin=True)
        self.client = APIClient()
        self.login_url = reverse('login')
        self.order_create_url = reverse('order-create')

    def authenticate(self, user):
        response = self.client.post(self.login_url, {'username': user.username, 'password': 'adminpass' if user.is_admin else 'pass'})
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_order(self):
        self.authenticate(self.user)
        response = self.client.post(self.order_create_url, {'title': 'Test Order', 'description': 'Order details'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

    def test_retrieve_order(self):
        self.authenticate(self.user)
        order = Order.objects.create(title='Read Test', description='Details', user=self.user)
        url = reverse('order-detail', kwargs={'pk': order.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Read Test')

    def test_update_order_by_owner(self):
        self.authenticate(self.user)
        order = Order.objects.create(title='Update Me', description='Old', user=self.user)
        url = reverse('order-detail', kwargs={'pk': order.id})
        response = self.client.put(url, {'title': 'Updated', 'description': 'New'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order.refresh_from_db()
        self.assertEqual(order.title, 'Updated')

    def test_delete_order_by_admin(self):
        order = Order.objects.create(title='To Delete', description='Admin job', user=self.user)
        self.authenticate(self.admin)
        url = reverse('order-detail', kwargs={'pk': order.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Order.objects.filter(id=order.id).exists())

    def test_update_order_by_non_owner(self):
        other_user = User.objects.create_user(username='other', password='pass')
        order = Order.objects.create(title='Blocked', description='No access', user=other_user)
        self.authenticate(self.user)
        url = reverse('order-detail', kwargs={'pk': order.id})
        response = self.client.put(url, {'title': 'Hack', 'description': 'Try update'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_order_by_non_admin(self):
        order = Order.objects.create(title='No Delete', description='Only admin', user=self.user)
        self.authenticate(self.user)
        url = reverse('order-detail', kwargs={'pk': order.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
