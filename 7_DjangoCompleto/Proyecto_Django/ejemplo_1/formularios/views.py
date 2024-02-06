from django.shortcuts import render

# Create your views here.
def formularios_inicio(request):
    return render(request, 'formularios/home.html',{})

def formularios_simple(request):
    return render(request, 'formularios/simple.html',{})

