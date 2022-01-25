from .models import User, CarBrand, CarModel, UserCar
from rest_framework import serializers


# User Model Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'bio', 'location']


# UserCar Model Serializer
class UserCarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserCar
        fields = ['url', 'user', 'car_brand', 'car_model', 'first_reg', 'odo', 'created_at']


# CarBrand Model Serializer
class CarBrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CarBrand
        fields = ['url', 'name']


# CarModel Model Serializer
class CarModelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CarModel
        fields = ['url', 'car_brand', 'name']


# Register User Serializer
class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user