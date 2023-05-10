
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/<name>', views.person_new),
    path('people', views.person_list),
]
