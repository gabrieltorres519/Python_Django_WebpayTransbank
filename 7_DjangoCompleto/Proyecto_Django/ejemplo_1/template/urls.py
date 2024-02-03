from django.urls import path
from .views import *
 
urlpatterns = [
    path('', template_inicio, name='template_inicio')
]

