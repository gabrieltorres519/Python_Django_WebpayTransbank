from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class Estado(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='nombre')
    # numero = models.PositiveIntegerField(default=0) # Cuando se agrega un nuevo campo después de crear la tabla se necesita darle un valor por defecto ya que no estaba contamplado


    def __str__(self):
        return self.nombre

    class Meta:
        # se trata del nombre que tendrá la tabla en la base
        db_table = 'estado'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados' 


class Genero(models.Model):
    nombre = models.CharField(max_length=100, null=True)
     
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'genero'
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'


class Pais(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'pais'
        verbose_name = 'País'
        verbose_name_plural = 'Países'


class Perfiles(models.Model):
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'perfil'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    slug = AutoSlugField(populate_from='nombre')


    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Producto(models.Model): 
    # Dado que el producto está relacionado con una categoría de producto y si se borra una categoría que esté siendo usada por un producto no se permitirá
    # Obviamente, como en sql, se pueden tener todas las llaves foráneas que se quieran, cuantas tablas relacionadas se necesiten
    # Las relaciones manejadas son 1 a muchos
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    nombre = models.CharField(max_length=100, null=True)
    slug = AutoSlugField(populate_from='nombre')
    fecha = models.DateTimeField(auto_now=True) # Enviando por defecto la fecha actual
    descripcion = models.TextField()
    #hora = models.TimeField(auto_now=True)
    #fecha = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Metadata(models.Model):
    description = models.CharField(max_length=255)
    keyword = models.TextField()
    correo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return self.correo

    class Meta:
        db_table = 'metadata'
        verbose_name = 'Metadata'
        verbose_name_plural = 'Metadata'

