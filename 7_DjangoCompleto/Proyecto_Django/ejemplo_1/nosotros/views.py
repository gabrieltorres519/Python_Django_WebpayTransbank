from django.shortcuts import render

# Create your views here.

def nosotros_inicio(request):
    return  render(request, 'nosotros/home.html', {}) 

