from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def diseno_inicio(request):
    # return HttpResponse("Hola mundo")
    return  render(request, 'diseno/home.html', {}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista

def diseno_ajax(request, id):
    # return HttpResponse("Hola mundo")
    return  render(request, 'diseno/ajax.html', {'id': id}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista


def diseno_modal(request, id):
    # return HttpResponse("Hola mundo")
    return  render(request, 'diseno/modal.html', {'id': id}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista


# En templates/home habrá un archivo por cada función definida aquí,
# pues esa función es la encargada de renderizar la vista