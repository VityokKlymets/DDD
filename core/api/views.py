from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Order
from .serializers import UserRegisterSerializer, UserLoginSerializer, OrderSerializer

# Register a new user
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

# Login and return JWT tokens
class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

# Create a new order (authenticated users only)
class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        order = super().get_object()
        if self.request.method == 'PUT' and order.user != self.request.user and not self.request.user.is_admin:
            raise PermissionDenied("Only the owner or an admin can update this order.")
        if self.request.method == 'DELETE' and not self.request.user.is_admin:
            raise PermissionDenied("Only an admin can delete this order.")
        return order

    def perform_update(self, serializer):
        serializer.save()