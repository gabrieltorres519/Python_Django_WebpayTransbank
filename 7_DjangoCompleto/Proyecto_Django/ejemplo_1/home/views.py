from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def home_inicio(request):
    # return HttpResponse("Hola mundo")
    return  render(request, 'home/home.html', {}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista

def home_nosotros(request):
    return  render(request, 'home/nosotros.html', {}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista

# En templates/home habrá un archivo por cada función definida aquí,
# pues esa función es la encargada de renderizar la vista