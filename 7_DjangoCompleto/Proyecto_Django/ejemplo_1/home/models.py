from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class Estado(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='nombre')
    numero = models.PositiveIntegerField(default=0) # Cuando se agrega un nuevo campo después de crear la tabla se necesita darle un valor por defecto ya que no estaba contamplado


    def __str__(self):
        return self.nombre

    class Meta:
        # se trata del nombre que tendrá la tabla en la base
        db_table = 'estado'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados' 