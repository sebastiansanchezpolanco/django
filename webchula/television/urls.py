from django.urls import path
from television import views
ulrpatterns=[
    path("index/", views.index, name="index"),
]