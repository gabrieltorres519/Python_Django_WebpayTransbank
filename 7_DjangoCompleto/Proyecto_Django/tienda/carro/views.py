from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from home.models import *
from acceso.decorators import logueado
from utilidades import utilidades, webpay
import json
from django.conf import settings

# Create your views here.
@logueado()
def carro_inicio(request):
    cuantos=Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).count()
    datos=Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).order_by('-id').all()
    suma=0
    for dato in datos:
        valor=dato.cantidad*dato.producto.precio
        suma=suma+valor
    return render(request, 'carro/home.html', {'datos': datos, 'suma': suma, 'cuantos': cuantos})


@logueado()
def carro_crear(request):
    if request.method =='POST':
        try:
            datos=Producto.objects.filter(pk=request.POST['id']).get()
        except Producto.DoesNotExist:
            raise Http404
        Carrito.objects.create(cantidad=request.POST['cantidad'], producto_id=request.POST['id'], users_metadata_id=request.session['users_metadata_id'])
        return HttpResponseRedirect("/carro")
    else:
        raise Http404
    

@logueado()
def carro_vaciar(request):
    Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).delete()
    OrdenDeCompra.objects.filter(users_metadata_id=request.session['users_metadata_id']).filter(estado_id=3).delete()
    
    messages.add_message(request, messages.SUCCESS, f'Se vació tu carrito exitosamente!!!.')
    return HttpResponseRedirect('/carro')


@logueado()
def carro_quitar(request, id):
    try:
        datos=Producto.objects.filter(pk=id).get()
    except Producto.DoesNotExist:
        raise Http404
    Carrito.objects.filter(users_metadata_id=request.session['users_metadata_id']).filter(producto_id=id).delete()
    messages.add_message(request, messages.SUCCESS, f'Se quitó el producto del carrito exitosamente!!!.')
    return HttpResponseRedirect('/carro')
