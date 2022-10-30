from django.urls import path
from cars_exam.cars.views import *


urlpatterns = (
    path("create/", create_car, name="create-car"),
    path("details/<pk>/", car_details, name="details-car"),
    path("edit/<pk>/", edit_car, name="edit-car"),
    path("delete/<pk>/", delete_car, name="delete-car"),
)
