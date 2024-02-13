# Generated by Django 3.0.5 on 2024-02-13 22:29

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
                'db_table': 'comuna',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'db_table': 'estado',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
                'db_table': 'genero',
            },
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(default='0')),
                ('correo', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Metadata',
                'verbose_name_plural': 'Metadata',
                'db_table': 'metadata',
            },
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_ws', models.CharField(default='0', max_length=255)),
                ('tarjeta', models.CharField(default='0', max_length=10)),
                ('fecha_transbank', models.CharField(default='0', max_length=100)),
                ('estado_transbank', models.CharField(default='0', max_length=100)),
                ('suma', models.PositiveIntegerField(default=0)),
                ('direccion', models.TextField(default='0')),
                ('observaciones', models.TextField(default='')),
                ('fecha', models.DateField(auto_now=True, null=True)),
                ('comuna', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Comuna')),
                ('estado', models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Estado')),
            ],
            options={
                'verbose_name': 'Orden de compra',
                'verbose_name_plural': 'Órdenes de compra',
                'db_table': 'orden_de_compra',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
                'db_table': 'pais',
            },
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'db_table': 'perfiles',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(default='200_200.png', upload_to='producto')),
                ('fecha', models.DateField(auto_now=True)),
                ('precio', models.PositiveIntegerField(default=0)),
                ('precio_antes', models.PositiveIntegerField(default=0)),
                ('sku', models.CharField(blank=True, default='1', max_length=100, null=True)),
                ('stock', models.PositiveIntegerField(default=1)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Estado')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'producto',
            },
        ),
        migrations.CreateModel(
            name='ProductoCategoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
            ],
            options={
                'verbose_name': 'Producto Categoría',
                'verbose_name_plural': 'Productos Categorías',
                'db_table': 'producto_categoria',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedor',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Región',
                'verbose_name_plural': 'Región',
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(default='edificacion.png', upload_to='slide')),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('target', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slide',
                'db_table': 'slide',
            },
        ),
        migrations.CreateModel(
            name='UsersMetadata',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=100, null=True)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('comuna', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Comuna')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Estado')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Genero')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Pais')),
                ('perfiles', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Perfiles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User metadata',
                'verbose_name_plural': 'User metadata',
                'db_table': 'users_metadata',
            },
        ),
        migrations.CreateModel(
            name='ProductoRecomendados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Producto')),
            ],
            options={
                'verbose_name': 'Producto recomendados',
                'verbose_name_plural': 'Productos recomendados',
                'db_table': 'producto_recomendados',
            },
        ),
        migrations.CreateModel(
            name='ProductoFotos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(default='200_200.png', upload_to='producto')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Producto')),
            ],
            options={
                'verbose_name': 'Producto fotos',
                'verbose_name_plural': 'Productos fotos',
                'db_table': 'producto_fotos',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='producto_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.ProductoCategoria'),
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Proveedor'),
        ),
        migrations.CreateModel(
            name='OrdenDeCompraDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('orden_de_compra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.OrdenDeCompra')),
                ('producto', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Producto')),
            ],
            options={
                'verbose_name': 'Orden de compra detalle',
                'verbose_name_plural': 'Órdenes de compra detalle',
                'db_table': 'orden_de_compra_detalle',
            },
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='users_metadata',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.UsersMetadata'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Region'),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('fecha', models.DateField(auto_now=True, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Producto')),
                ('users_metadata', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.UsersMetadata')),
            ],
            options={
                'verbose_name': 'Carrito',
                'verbose_name_plural': 'Carrito',
                'db_table': 'carrito',
            },
        ),
    ]
