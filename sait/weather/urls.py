
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('delete/<str:city>/', views.Delete),
    path('map/', views.map)
]
