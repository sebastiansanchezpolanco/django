from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Creamos un metodo para dibujar las vistas
def index(request):
    return render(request, "paginas/index.html")

def mascotas(request):
    mascotas = [
    {"nombre": "Max", "raza": "Golden Retriever", "edad": 3},
    {"nombre": "Luna", "raza": "Siamés", "edad": 2},
    {"nombre": "Rocky", "raza": "Bulldog Francés", "edad": 5},
    {"nombre": "Mora", "raza": "Labrador", "edad": 1},
    {"nombre": "Simba", "raza": "Persa", "edad": 4},
    {"nombre": "Coco", "raza": "Poodle", "edad": 6},
    {"nombre": "Toby", "raza": "Beagle", "edad": 2},
    {"nombre": "Bella", "raza": "Chihuahua", "edad": 7},
    {"nombre": "Thor", "raza": "Pastor Alemán", "edad": 4},
    {"nombre": "Mimi", "raza": "Bengala", "edad": 3},
    {"nombre": "Bruno", "raza": "Boxer", "edad": 5},
    {"nombre": "Nala", "raza": "Maine Coon", "edad": 2},
    {"nombre": "Cooper", "raza": "Border Collie", "edad": 3},
    {"nombre": "Lola", "raza": "Dachshund", "edad": 8},
    {"nombre": "Zeus", "raza": "Rottweiler", "edad": 6},
    {"nombre": "Maya", "raza": "Husky Siberiano", "edad": 4},
    {"nombre": "Bobi", "raza": "Mestizo", "edad": 10},
    {"nombre": "Kira", "raza": "Shiba Inu", "edad": 3},
    {"nombre": "Paco", "raza": "Loro Gris", "edad": 15},
    {"nombre": "Pelusa", "raza": "Angora", "edad": 5},
    {"nombre": "Apolo", "raza": "Gran Danés", "edad": 4},
    {"nombre": "Daisy", "raza": "Cocker Spaniel", "edad": 6},
    {"nombre": "Jack", "raza": "Jack Russell", "edad": 2},
    {"nombre": "Cleo", "raza": "Esfinge", "edad": 3},
    {"nombre": "Rocco", "raza": "Doberman", "edad": 5},
    {"nombre": "Nina", "raza": "Yorkshire Terrier", "edad": 9},
    {"nombre": "Oliver", "raza": "Tabby", "edad": 4},
    {"nombre": "Milo", "raza": "Pug", "edad": 3},
    {"nombre": "Sasha", "raza": "Samoyedo", "edad": 5},
    {"nombre": "Tano", "raza": "Pitbull", "edad": 4},
    {"nombre": "Gala", "raza": "Galgo", "edad": 6},
    {"nombre": "Ramón", "raza": "Bulldog Inglés", "edad": 7},
    {"nombre": "Sora", "raza": "Akita", "edad": 3},
    {"nombre": "Bimba", "raza": "Shih Tzu", "edad": 5},
    {"nombre": "Fito", "raza": "Schnauzer", "edad": 2},
    {"nombre": "Cloe", "raza": "Ragdoll", "edad": 4},
    {"nombre": "Duke", "raza": "Mastín", "edad": 6},
    {"nombre": "Kaiser", "raza": "Pastor Belga", "edad": 5},
    {"nombre": "Lulú", "raza": "Pomerania", "edad": 3},
    {"nombre": "Romeo", "raza": "British Shorthair", "edad": 2},
    {"nombre": "Oreo", "raza": "Border Collie", "edad": 1},
    {"nombre": "Akira", "raza": "Pinscher", "edad": 4},
    {"nombre": "Benito", "raza": "Basset Hound", "edad": 6},
    {"nombre": "Zoe", "raza": "Maltés", "edad": 5},
    {"nombre": "Tito", "raza": "Canario", "edad": 1},
    {"nombre": "Blanca", "raza": "Samoyedo", "edad": 3},
    {"nombre": "Ringo", "raza": "Dálmata", "edad": 4},
    {"nombre": "Minerva", "raza": "Azul Ruso", "edad": 7},
    {"nombre": "Hércules", "raza": "San Bernardo", "edad": 5},
    {"nombre": "Pepe", "raza": "Tortuga", "edad": 20}
    ]
    informacion={
        "listamascotas":mascotas
    }
    return render(request, "paginas/mascotas.html", informacion)

def colores(request):
    if ('micolor' in request.GET):
        colorRecibido=request.GET["micolor"]
    else:
        colorRecibido="NADA DE NADA!"
    informacion={
        "color":colorRecibido,
    }
    return render(request, "paginas/colores.html", informacion)