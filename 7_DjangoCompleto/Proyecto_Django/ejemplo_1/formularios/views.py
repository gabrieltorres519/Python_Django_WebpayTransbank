from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages 
from home.models import *

# Create your views here.
def formularios_inicio(request):
    return render(request, 'formularios/home.html',{})

def formularios_simple(request):
    if request.method == 'POST':
        #return HttpResponse(f"El valor de nombre es {request.POST['nombre']}")
        descripcion = f"El valor de nombre es {request.POST['nombre']}, correo={request.POST['correo']},  mensaje={request.POST['mensaje']}"
        Tracking.objects.create(descripcion = descripcion) # Haciendo un insert en el campo descripción de la tabla Tracking
    return render(request, 'formularios/simple.html',{})

