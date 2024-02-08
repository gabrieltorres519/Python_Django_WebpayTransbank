from django.urls import path
from .views import *
 
urlpatterns = [
    path('', consultas_inicio, name='consultas_inicio'),
	path('/add', consultas_add, name="consultas_add"),
	path('/add_atributos/<int:id>', consultas_add_atributos, name="consultas_add_atributos"),
    path('/buscador', consultas_buscador, name='consultas_buscador'),
    path('/productos-por-categoria/<str:slug>', consultas_productos_por_categoria, name='consultas_productos_por_categoria'),
    path('/productos-por-categoria-detalle/<int:id>/<str:slug>', consultas_productos_detalle, name='consultas_productos_detalle')
]

