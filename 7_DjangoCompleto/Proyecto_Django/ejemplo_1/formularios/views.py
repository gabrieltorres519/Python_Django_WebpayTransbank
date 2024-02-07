from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages 

# Create your views here.
def formularios_inicio(request):
    return render(request, 'formularios/home.html',{})

def formularios_simple(request):
    if request.method == 'POST':
        return HttpResponse(f"El valor de nombre es {request.POST['nombre']}")
    return render(request, 'formularios/simple.html',{})

