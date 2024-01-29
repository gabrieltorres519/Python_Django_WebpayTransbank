from django.urls import path
from .views import *
 
urlpatterns = [
    path('', nosotros_inicio, name='nosotros_inicio'),
    path('/nuestro-equipo', nosotros_nuestro_equipo, name='nosotros_nuestro_equipo')
]

