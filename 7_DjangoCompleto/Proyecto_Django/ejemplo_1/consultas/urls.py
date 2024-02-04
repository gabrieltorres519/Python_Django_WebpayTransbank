from django.urls import path
from .views import *
 
urlpatterns = [
    path('', consultas_inicio, name='consultas_inicio'),
    path('/productos-por-categoria/<str:slug>', consultas_productos_por_categoria, name='consultas_productos_por_categoria')
]

