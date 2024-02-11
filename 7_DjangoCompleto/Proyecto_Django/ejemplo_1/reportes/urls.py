from django.urls import path
from .views import *
 
urlpatterns = [
    path('', reportes_inicio, name='reportes_inicio'),
    path('/pdf', reportes_pdf, name='reportes_pdf'),

]

