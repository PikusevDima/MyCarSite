
from django.urls import path
from .views import views
from .views import person_view

urlpatterns = [
    path('', views.index),
    path('user/new/<name>', person_view.add_user),
    path('user/edit/<name>', person_view.edit_user),
    path('user', person_view.user_list),
    path('create_user', person_view.add_user),
]
