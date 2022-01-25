from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Changes the behavior of the standard Manager - filters out the soft deleted objects
class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


# Abstract Soft Delete model inherited by the other models
class SoftDeleteModel(models.Model):

    deleted_at = models.DateTimeField(null=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def delete(self):
        self.deleted_at = datetime.now()
        self.save()

    def hard_delete(self):
        super(SoftDeleteModel, self).delete()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


# User Model with soft delete functionality
class User(AbstractUser):

    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    deleted_at = models.DateTimeField(null=True, default=None)

    def delete(self):
        self.deleted_at = datetime.now()
        self.save()

    def hard_delete(self):
        super(SoftDeleteModel, self).delete()

    def restore(self):
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.username


# Car Brand Model
class CarBrand(SoftDeleteModel):

    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#Car Model Model
class CarModel(SoftDeleteModel):

    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='car_models')
    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# User Car Model
class UserCar(SoftDeleteModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cars')
    car_brand = models.ManyToManyField(CarBrand)
    car_model = models.ManyToManyField(CarModel)
    first_reg = models.DateField()
    odo = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']