from django.shortcuts import render
from django.http import HttpResponse, Http404
from home.models import *
# Create your views here.

def consultas_inicio(request):
    categorias = Categoria.objects.all()
    return  render(request, 'consultas/home.html', {'categorias':categorias}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista


# En templates/home habrá un archivo por cada función definida aquí,
# pues esa función es la encargada de renderizar la vista