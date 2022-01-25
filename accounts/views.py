from .models import User, CarBrand, CarModel, UserCar
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly, IsUserOrReadOnly
from url_filter.integrations.drf import DjangoFilterBackend
from .serializers import UserSerializer, UserCarSerializer, CarBrandSerializer, CarModelSerializer, RegisterUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.filter(deleted_at__isnull=True).order_by('-username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['username', 'email']


class UserCarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user cars to be viewed or edited.
    """

    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user', 'car_brand', 'car_model', 'first_reg', 'odo', 'created_at']


class CarBrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car brands to be viewed or edited.
    """

    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']


class CarModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car models to be viewed or edited.
    """

    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['car_brand','name']


class RegisterUserView(generics.CreateAPIView):
    """
    API endpoint that allows new users to register
    """

    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny, )