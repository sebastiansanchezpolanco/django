#Rutas para mi servidro http://paco
from django.urls import path
#Los metodos que tenemos en views.py
from mascotas import views
#Creamos las rutas 
urlpatterns=[ 
        path('index', views.index, name="index"),
        path('mascotas', views.mascotas, name="mascotas"),
        path('colores', views.colores, name="colores")
        ]