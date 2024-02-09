from django.urls import path
from .views import *
 
urlpatterns = [
    path('', formularios_inicio, name='formularios_inicio'),
    path('/simple', formularios_simple, name='formularios_simple'),
    path('/form', formularios_form, name='formularios_form'),
    path('/login', formularios_login, name='formularios_login'),
    path('/logueado', formularios_logueado, name='formularios_logueado'),
    path('/logueado-salir', formularios_logueado_salir, name="formularios_logueado_salir")
]

