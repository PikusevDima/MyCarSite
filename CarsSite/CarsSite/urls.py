
from django.urls import path
from .views import views
from .views import brand_view, car_view, person_view

urlpatterns = [
    path('', views.index),
    path('user', person_view.user_list),
    path('user/add', person_view.add_user),
    path('user/edit/<id>', person_view.edit_user),
    path('user/delete/<id>', person_view.delete_user),
    path('create_brand', brand_view.add_brand),
    path('car/add', car_view.new_car),
    path('car', car_view.list_car),
]
