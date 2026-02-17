from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Creamos un metodo para dibujar las vistas
def index(request):
    return HttpResponse("hoy es martes")

def prueba(request):
    return HttpResponse("probando probando...")
# Create your views here.
