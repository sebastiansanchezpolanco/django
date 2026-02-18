#Rutas para mi servidro http://paco
from django.urls import path
#Los metodos que tenemos en views.py
from aplicacion import views
#Creamos las rutas 
urlpatterns=[ 
        path('', views.index, name="index"),
        path('prueba/', views.prueba, name="prueba"),
        path('imagenes/', views.imagenes, name="imag"),
        path('futbol/', views.futbol, name="futbol"),
        path('nombres/', views.nombre, name="nombres")
        ]

