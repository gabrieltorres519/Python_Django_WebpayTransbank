# Generated by Django 3.0.5 on 2024-01-30 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_categoria_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_nacimiento', models.DateField(default='2001-08-22')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Genero')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Pais')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User metadata',
                'verbose_name_plural': 'Users metadata',
                'db_table': 'users_metadata',
            },
        ),
    ]
