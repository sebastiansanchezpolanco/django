#Rutas para mi servidro http://paco
from django.urls import path
#Los metodos que tenemos en views.py
from mascotas import views
#Creamos las rutas 
urlpatterns=[ 
        path('', views.mascotas, name="mascotas"),

        ]