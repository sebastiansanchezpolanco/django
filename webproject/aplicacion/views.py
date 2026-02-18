from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Creamos un metodo para dibujar las vistas
def index(request):
    return render(request, "paginas/index.html")

def prueba(request):
    return render(request, "paginas/prueba.html")

def imagenes(request):
    return render(request, "paginas/imag.html")

def futbol(request):
    informacion={
        "equipo": "Real Madrid"
    }
    return render(request, "paginas/futbol.html", informacion)

def nombre(request):
    jugadores = [
        "Neto Volpi", "Luis Marquinez", "Gali Balanta", "Juan Covilla", 
        "Anderson Angulo", "Jan Carlos Angulo Rosales", "Daniel Pedrozo", 
        "Yhorman Hurtado", "Juan José Mera", "Shean Barbosa", "Juan Pablo Torres", 
        "Cristian Arrieta", "Bryan Rovira", "Cristian Trujillo", "Junior Hernández", 
        "Jersson González", "Juan Pablo Nieto", "Sebastián Guzmán", "Ever Valencia", 
        "Elan Ricardo", "Victor Reyes", "Michael Martínez", "Yoimar Estiven Moreno", 
        "Jhon Alexander Quiñones", "Luis 'El Chino' Sandoval", "Edward López", 
        "Kelvin Javier Flórez Mosquera", "Jáder Valencia", "Gonzalo Lencina", 
        "Jeinner Fuentes", "Adrián Parra"
    ]
    plantilla = [
        {"nombre": "Neto Volpi", "posicion": "arquero"},
        {"nombre": "Luis Marquinez", "posicion": "arquero"},
        {"nombre": "Gali Balanta", "posicion": "arquero"},
        {"nombre": "Juan Covilla", "posicion": "arquero"},
        {"nombre": "Anderson Angulo", "posicion": "defensa"},
        {"nombre": "Jan Carlos Angulo Rosales", "posicion": "defensa"},
        {"nombre": "Daniel Pedrozo", "posicion": "defensa"},
        {"nombre": "Yhorman Hurtado", "posicion": "defensa"},
        {"nombre": "Juan José Mera", "posicion": "defensa"},
        {"nombre": "Shean Barbosa", "posicion": "defensa"},
        {"nombre": "Juan Pablo Torres", "posicion": "defensa"},
        {"nombre": "Cristian Arrieta", "posicion": "defensa"},
        {"nombre": "Bryan Rovira", "posicion": "medio campo"},
        {"nombre": "Cristian Trujillo", "posicion": "medio campo"},
        {"nombre": "Junior Hernández", "posicion": "medio campo"},
        {"nombre": "Jersson González", "posicion": "medio campo"},
        {"nombre": "Juan Pablo Nieto", "posicion": "medio campo"},
        {"nombre": "Sebastián Guzmán", "posicion": "medio campo"},
        {"nombre": "Ever Valencia", "posicion": "medio campo"},
        {"nombre": "Elan Ricardo", "posicion": "medio campo"},
        {"nombre": "Victor Reyes", "posicion": "medio campo"},
        {"nombre": "Michael Martínez", "posicion": "medio campo"},
        {"nombre": "Yoimar Estiven Moreno", "posicion": "medio campo"},
        {"nombre": "Jhon Alexander Quiñones", "posicion": "medio campo"},
        {"nombre": "Luis 'El Chino' Sandoval", "posicion": "delantero"},
        {"nombre": "Edward López", "posicion": "delantero"},
        {"nombre": "Kelvin Javier Flórez Mosquera", "posicion": "delantero"},
        {"nombre": "Jáder Valencia", "posicion": "delantero"},
        {"nombre": "Gonzalo Lencina", "posicion": "delantero"},
        {"nombre": "Jeinner Fuentes", "posicion": "delantero"},
        {"nombre": "Adrián Parra", "posicion": "delantero"}
    ]
    informacion={
        "listajugadores":jugadores,
        "plantilla":plantilla
    }
    return render(request, "paginas/nombres.html", informacion)