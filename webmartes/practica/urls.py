from django.urls import path
from . import views

urlpatterns = [
    path('hoy/', views.index, name='index'),
]
