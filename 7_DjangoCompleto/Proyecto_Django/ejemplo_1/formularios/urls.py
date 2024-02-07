from django.urls import path
from .views import *
 
urlpatterns = [
    path('', formularios_inicio, name='formularios_inicio'),
    path('/simple', formularios_simple, name='formularios_simple'),
    path('/form', formularios_form, name='formularios_form'),
]

