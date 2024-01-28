from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def home_inicio(request):
    return HttpResponse("Hola mundo")