# Cars API with Soft Delete
## Project description:
The project is created with Django REST framework. For all users the API gives read-only access to lists of Cars, Users, Car brands and Car models. Users who are logged in can edit their own profiles and create Car, Car brands and Car models objects. Users can navigate between the objects through links.

## Project files:

### accounts:
1. models.py - contains all models
* User
* UserCar
* CarBrand
* CarModel
* SoftDeleteModel - inherited by the other models in order to handle the soft delete functionality
* SoftDeleteManager - changes the behavior of the standard Manager - filters out the soft deleted objects
2. permissions.py - contains two custom permissions
* IsOwnerOrReadOnly - custom permission to only allow owners of a car object to edit it
* IsUserOrReadOnly - custom permission to only allow owners of a profile to edit it
3. serializers.py - contains the serializers of the models
* UserSerializer
* UserCarSerializer
* CarBrandSerializer
* CarModelSerializer
* RegisterUserSerializer
4. views.py 
* UserViewSet
* UserCarViewSet
* CarBrandViewSet
* CarModelViewSet
* RegisterUserView

### cars:
1. urls.py
