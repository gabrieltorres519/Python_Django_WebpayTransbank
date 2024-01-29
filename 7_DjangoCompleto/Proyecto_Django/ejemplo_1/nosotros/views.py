from django.shortcuts import render

# Create your views here.

def nosotros_inicio(request):
    return  render(request, 'nosotros/home.html', {}) 

def nosotros_nuestro_equipo(request):
    return render(request, 'nosotros/nuestro_equipo.html', {}) 

