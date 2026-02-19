from django.urls import path
from formulario import views

urlpatterns =[
    path('', views.index, name="index"),
    path('ejemplo/', views.ejemplo, name="ejemplo"),
    path('saludos/', views.saludo, name="saludo"),
    path('suma/', views.suma, name="suma"),
    path('parimpar/', views.parimpar, name="parimpar"),
    path('collatz/', views.collatz, name="collatz")
]
