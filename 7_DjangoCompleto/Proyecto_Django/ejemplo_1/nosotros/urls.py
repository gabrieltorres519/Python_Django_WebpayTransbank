from django.urls import path
from .views import *
 
urlpatterns = [
    path('', nosotros_inicio, name='nosotros_inicio'),
]

