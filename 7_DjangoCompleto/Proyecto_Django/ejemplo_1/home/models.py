from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estado(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        # se trata del nombre que tendrá la tabla en la base
        db_table = 'estado'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados' 