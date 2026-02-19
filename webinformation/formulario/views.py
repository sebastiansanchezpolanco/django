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
    
def suma(request):
    if('cajanum1' in request.POST):
        num1=request.POST["cajanum1"]
        num2=request.POST["cajanum2"]
        suma=int(num1)+int(num2)
        informacion={
            "suma":suma
        }
        return render(request, "paginas/suma.html", informacion)
    else:
        return render(request, "paginas/suma.html")
def parimpar(request):
    if('cajanum1' in request.POST):
        num1=request.POST["cajanum1"]
        verificador=int(num1)%2
        if (verificador==0):
            informacion={
            "verific":"par"
        }
        else:
            (verificador!=0)
            informacion={
            "verific":"impar"
        }
        return render(request, "paginas/parimpar.html", informacion)
    else:
        return render(request, "paginas/parimpar.html")