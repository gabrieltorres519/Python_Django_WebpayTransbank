from django.urls import path
from .views import *
 
urlpatterns = [
    path('', reportes_inicio, name='reportes_inicio'),
    path('/pdf', reportes_pdf, name='reportes_pdf'),
    path('/importar-excel', reportes_importar_excel, name='reportes_importar_excel'),
    path('/importar-txt', reportes_importar_txt, name='reportes_importar_txt'),
]

