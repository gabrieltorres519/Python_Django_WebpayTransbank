from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages 
from home.models import *
from .forms import *

# Create your views here.
def formularios_inicio(request):
    return render(request, 'formularios/home.html',{})

def formularios_form(request):
	#form = Formulario_ejemplo(request.POST or None)
	if request.method =='POST':
		form = Formulario_ejemplo(request.POST or None)
		if form.is_valid():
			data = form.cleaned_data
			descripcion=f"el valor de nombre es {data['nombre']}, correo={data['correo']}, teléfono={data['telefono']}, mensaje={data['mensaje']}" # Los campos data['name'] sustituyen a request.POST['name']
			save = Tracking() # En lugar de usar la tabla Traking.objects.create()  
			save.descripcion= descripcion # Así accedemos la tabla tracking como objeto.campo
			save.save()
			messages.add_message(request, messages.SUCCESS, f"Gracias por escribirnos, nos pondremos en contacto a la brevedad, sonría que es gratis!!!")
			return HttpResponseRedirect(f"/formularios/form")
	else:
		form = Formulario_ejemplo()
	return render(request, 'formularios/form.html', {'form':form})

def formularios_simple(request):
    if request.method == 'POST':
        #return HttpResponse(f"El valor de nombre es {request.POST['nombre']}")
        descripcion = f"El valor de nombre es {request.POST['nombre']}, correo={request.POST['correo']},  mensaje={request.POST['mensaje']}"
        Tracking.objects.create(descripcion = descripcion) # Haciendo un insert en el campo descripción de la tabla Tracking
        messages.add_message(request,messages.SUCCESS,f"Gracias por escribirnos, nos pondremos en contacto a la brevedad, sonría que es gratis!!")
        return HttpResponseRedirect(f"/formularios/simple") # Para evitar que la petición se mantenga guardada en la vista
    return render(request, 'formularios/simple.html',{})

