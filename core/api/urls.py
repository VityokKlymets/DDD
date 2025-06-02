from django.urls import path
from .views import RegisterView, LoginView, OrderCreateView,OrderRetrieveUpdateDeleteView

urlpatterns = [
    path('users/register', RegisterView.as_view(), name='register'),
    path('users/login', LoginView.as_view(), name='login'),
    path('orders', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>', OrderRetrieveUpdateDeleteView.as_view(), name='order-detail'),
]
