"""ejemplo_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('core/backend/', admin.site.urls),
    path('', include('home.urls'), name='home_urls'),
    path('nosotros', include('nosotros.urls'), name='nosotros_urls'),
    path('diseno', include('diseno.urls'), name='diseno_urls'),
    path('template', include('template.urls'), name='template_urls'),
    path('consultas', include('consultas.urls'), name='consultas_urls'),
    path('formularios', include('formularios.urls'), name='formularios_urls'),
    path('reportes', include('reportes.urls'), name='reportes_urls'),
]
