from django.urls import path
from .views import *
 
urlpatterns = [
    path('', consultas_inicio, name='consultas_inicio')
]

