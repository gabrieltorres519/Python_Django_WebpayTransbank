from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
#signal
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

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


class UsersMetadata(models.Model):
    pais = models.ForeignKey(Pais, models.DO_NOTHING) # Relación con la tabla país, para indicar de qué país es el usuario, de los contemplados en la base
    user = models.ForeignKey(User, models.DO_NOTHING) # Esta relación es muy importante para agregar cosas a la tabla de usuarios de django, porque no la podemos modificar
    genero = models.ForeignKey(Genero, models.DO_NOTHING)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(default='2001-08-22')



    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        db_table = 'users_metadata'
        verbose_name = 'User metadata'
        verbose_name_plural = 'Users metadata' 
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    slug = AutoSlugField(populate_from='nombre')


    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Tracking(models.Model):
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tracking'
        verbose_name = 'Tracking'
        verbose_name_plural = 'Trackings'


class Producto(models.Model): 
    # Dado que el producto está relacionado con una categoría de producto y si se borra una categoría que esté siendo usada por un producto no se permitirá
    # Obviamente, como en sql, se pueden tener todas las llaves foráneas que se quieran, cuantas tablas relacionadas se necesiten
    # Las relaciones manejadas son 1 a muchos
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    nombre = models.CharField(max_length=100, null=True)
    slug = AutoSlugField(populate_from='nombre')
    fecha = models.DateTimeField(auto_now=True) # Enviando por defecto la fecha actual
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="producto", default="default.jpg") # pip install Pillow Upload_to es el nombre de la carpeta a donde se moverá la imágen ya que esté en el servidor
    #hora = models.TimeField(auto_now=True)
    #fecha = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


@receiver(post_save, sender=Producto)
def producto_save(sender, instance, **kwargs):
    if kwargs['created']:
        Tracking.objects.create(descripcion=f"se creó el producto con el id {instance.id}")


@receiver(pre_save, sender=Producto)
def producto_change(sender, instance: Producto, **kwargs):
    if instance.id is None:
        pass
    else:
        previus = Producto.objects.get(id=instance.id)
        if previus.nombre != instance.nombre:
            Tracking.objects.create(descripcion=f"se modificó el producto con el id {instance.id}")


@receiver(pre_delete, sender=Producto)
def producto_delete(sender, instance: Producto, **kwargs):
    if instance.id is None:
        pass
    else:
        Tracking.objects.create(descripcion=f"se eliminó el producto con el id {instance.id}")


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

