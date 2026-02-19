from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "paginas/index.html")
def ejemplo(request):
    return render(request, "paginas/ejemplo.html")
def saludo(request):
    if('cajanombre' in request.POST):
        dato=request.POST["cajanombre"]
        informacion={
            "nombre":dato
        }
        return render(request, "paginas/saludo.html", informacion)
    else:
        return render(request, "paginas/saludo.html")