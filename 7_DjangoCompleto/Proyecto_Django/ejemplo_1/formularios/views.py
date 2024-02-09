from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages 
from home.models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from formularios.decorators import logueada

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


def formularios_login(request):
	form = Formulario_Login(request.POST or None)
	if request.method=='POST':
		if form.is_valid:
			#data = form.cleaned_data
			user =authenticate(request, username=request.POST['correo'], password=request.POST['password'])
			if user is not None:
				login(request, user)
				usersMetadata=UsersMetadata.objects.filter(user_id=request.user.id).get()
				request.session['users_metadata_id']=usersMetadata.id
				return HttpResponseRedirect('/formularios/logueado')
			else:
				messages.add_message(request, messages.WARNING, f'Los datos ingresados no son correctos, por favor vuelva a intentar.')
				return HttpResponseRedirect('/formularios/login')
	return render(request, 'formularios/login.html', {'form': form})

@logueada()
def formularios_logueado(request):
	return render(request, 'formularios/logueado.html', {})

def formularios_logueado_salir(request):
	logout(request)
	###sólo si creaste variables de sesión
	try:
		del request.session['users_metadata_id'] 
	except KeyError:
		pass
	##ésto si va si o si para que no te enredes, sonríe que es gratis
	messages.add_message(request, messages.WARNING, f'Se cerró la sesión exitosamente.')
	return HttpResponseRedirect('/formularios/login')