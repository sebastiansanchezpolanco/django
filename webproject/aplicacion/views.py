from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Creamos un metodo para dibujar las vistas
def index(request):
    return render(request, "paginas/index.html")

def prueba(request):
    return render(request, "paginas/prueba.html")

def prueba(request):
    return render(request, "paginas/imag.html")