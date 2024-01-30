from django.urls import path
from .views import *
 
urlpatterns = [
    path('', diseno_inicio, name='diseno_inicio'),
    path('/ajax/<int:id>', diseno_ajax, name='diseno_ajax'),
]

