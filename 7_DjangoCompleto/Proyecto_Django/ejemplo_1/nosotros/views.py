from django.shortcuts import render

# Create your views here.

def nosotros_inicio(request):
    return  render(request, 'nosotros/home.html', {}) 

def nosotros_nuestro_equipo(request):
    return render(request, 'nosotros/nuestro_equipo.html', {}) 

def nosotros_nuestro_equipo_detalle(request, id, slug):
    nombre = 'Mauricio Pérez'
    estaciones = ["Primavera","Verano","Otoño","Invierno"]
    return render(request, 'nosotros/nuestro_equipo_detalle.html', {'id':id, 'slug':slug, 'nombre':nombre, 'estaciones':estaciones}) 
