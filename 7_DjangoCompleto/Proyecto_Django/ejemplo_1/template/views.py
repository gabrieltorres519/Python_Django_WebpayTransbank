from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def template_inicio(request):
    listas = ["uno","dos","tres", "cuatro", "gato", "ave"]
    texto = "<h1> tss </h1>"
    foto = "1706839318.193531.jpg"
    color = "rojo" 
    return  render(request, 'template/home.html', {'listas': listas, 'texto': texto, 'foto': foto, 'color': color}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista


# En templates/home habrá un archivo por cada función definida aquí,
# pues esa función es la encargada de renderizar la vista