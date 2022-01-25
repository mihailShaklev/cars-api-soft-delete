"""cars URL Configuration"""

from django.urls import include, path
from rest_framework import routers
from accounts.views import *


# Declare a default router and register the views
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cars', UserCarViewSet)
router.register(r'brands', CarBrandViewSet)
router.register(r'models', CarModelViewSet)



# Include the default router in the url patterns
urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterUserView.as_view()),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
