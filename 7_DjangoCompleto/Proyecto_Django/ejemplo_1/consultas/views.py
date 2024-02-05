from django.shortcuts import render
from django.http import HttpResponse, Http404
from home.models import *
from utilidades import utilidades
# Create your views here.

def consultas_inicio(request):
    categorias = Categoria.objects.order_by('-id').all()
    total = Producto.objects.order_by('-id').all()
    paginar = utilidades.get_paginacion(total,request)
    return  render(request, 'consultas/home.html', {'categorias':categorias, 'total': total, 'datos': paginar[0], 'numeros': paginar[1], 'page': paginar[2] }) # contiene la ruta del template de esa vista y los datos que se quieren renderizar en la vista

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