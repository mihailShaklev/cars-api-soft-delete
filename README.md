# Cars API with Soft Delete
## Project description:
The project is created with Django REST framework. For all users the API gives read-only access to lists of Cars, Users, Car brands and Car models. Users who are logged in can edit their own profiles and create Car, Car brands and Car models objects. Users can navigate between the objects through links.

## Project files:
### accounts app:
1.models.py - contains all models
*User
*UserCar
*CarBrand
*CarModel
*SoftDeleteModel - inherited by the other models in order to handle the soft delete functionality
*SoftDeleteManager - changes the behavior of the standard Manager - filters out the soft deleted objects
