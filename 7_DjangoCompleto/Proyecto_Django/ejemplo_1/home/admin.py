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


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', formularios.set_categoria_con_link, 'nombre', 'fecha', 'descripcion')
    search_fields = ('id', 'nombre')

    class Media:
        js = (
            '/assets/tiny_mce/tiny_mce.js',
            '/assets/tiny_mce/textarea.js',
        )


admin.site.register(Estado, EstadoAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Perfiles, PerfilesAdmin)
admin.site.register(UsersMetadata, UsersMetadataAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)

admin.site.site_header = 'Backend Ejemplo 1'
admin.site.index_title = 'Backend Ejemplo 1'
admin.site.site_title = 'Backend Ejemplo 1'