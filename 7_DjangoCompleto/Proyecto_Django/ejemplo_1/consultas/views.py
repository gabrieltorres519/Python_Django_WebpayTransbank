from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from home.models import *
from utilidades import utilidades
from .forms import *
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime, date, timedelta
from django.contrib import messages
from utilidades import utilidades, dreamhost

# Create your views here.

def consultas_inicio(request):
    categorias = Categoria.objects.order_by('-id').all()
    total = Producto.objects.order_by('-id').all()
    paginar = utilidades.get_paginacion(total,request)
    return  render(request, 'consultas/home.html', {'categorias':categorias, 'total': total, 'datos': paginar[0], 'numeros': paginar[1], 'page': paginar[2] }) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista

def consultas_add(request):
	if request.method =='POST':
		form=Formulario_producto(request.POST, request.FILES)
		if request.POST['foto']=='vacio':
			foto = "default.png"
		else:
			myfile = request.FILES['file']
			if utilidades.getExtension(request.FILES['file']):
				fs = FileSystemStorage()
				fecha=datetime.now()
				foto = f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['file']))[1]}"
				filename=fs.save(f"producto/{foto}", myfile)
				uploaded_file_url=fs.url(filename)
				dreamhost.moverArchivoProducto2(foto)
			else:
				mensaje = f"El archivo para la foto no es válido, debe ser JPG|PNG|GIF."
				messages.add_message(request, messages.WARNING, mensaje)
				return HttpResponseRedirect(f'/consultas/add')
		Producto.objects.create(nombre=request.POST['nombre'], precio=request.POST['precio'], descripcion=request.POST['descripcion'], foto=foto, categoria_id=request.POST['categoria'])
		messages.add_message(request, messages.SUCCESS, f"Se creó el registro exitosamente")
		return HttpResponseRedirect(f'/consultas/add')
	else:
		form=Formulario_producto() 
	return render(request, 'consultas/add.html', {'form':form})


def consultas_buscador(request):
	if not request.GET.get('b'):
		b=''
	else:
		b=request.GET.get('b')
	categorias = Categoria.objects.order_by('nombre').all()
	total = Producto.objects.filter(nombre__icontains=b).order_by('-id').all()
	paginar = utilidades.get_paginacion(total, request)
	return render(request, 'consultas/buscador.html', {'categorias':categorias, 'total':total, 'datos':paginar[0], 'numeros':paginar[1], 'page':paginar[2], 'b': b})

def consultas_productos_por_categoria(request, slug):
    try:
        cat = Categoria.objects.filter(slug = slug).get() # Consulta para un solo registro
    except Categoria.DoesNotExist:
        raise Http404
     
    categorias = Categoria.objects.order_by('nombre').all()
    datos = Producto.objects.filter(categoria_id=cat.id).all()
    return  render(request, 'consultas/productos_por_categoria.html', {'categorias':categorias, 'cat':cat, 'datos':datos}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista

def consultas_productos_detalle(request, id, slug):
    try:
        producto = Producto.objects.filter(slug = slug, id=id).get() # Consulta para un solo registro
    except Categoria.DoesNotExist:
        raise Http404
    
    categorias = Categoria.objects.order_by('nombre').all()
    return  render(request, 'consultas/productos_detalle.html', {'categorias':categorias, 'producto':producto}) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista



# En templates/home habrá un archivo por cada función definida aquí,
# pues esa función es la encargada de renderizar la vista