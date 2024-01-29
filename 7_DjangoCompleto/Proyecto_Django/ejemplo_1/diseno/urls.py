from django.urls import path
from .views import *
 
urlpatterns = [
    path('', diseno_inicio, name='diseno_inicio')
]

