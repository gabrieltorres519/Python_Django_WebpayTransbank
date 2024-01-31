from django.contrib import admin
from home.models import *
from utilidades import formularios

# Agregamos la configuración para poder tener en la vista la tabla Estado
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields = ('id','nombre')


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')


class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')


class PerfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')


class UsersMetadataAdmin(admin.ModelAdmin):
    list_display = ('id', 'telefono', 'genero', formularios.set_user, 'fecha_nacimiento')


admin.site.register(Estado, EstadoAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Perfiles, PerfilesAdmin)
admin.site.register(UsersMetadata, UsersMetadataAdmin)

admin.site.site_header = 'Backend Ejemplo 1'
admin.site.index_title = 'Backend Ejemplo 1'
admin.site.site_title = 'Backend Ejemplo 1'