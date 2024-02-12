# Generated by Django 3.0.5 on 2024-02-11 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_prodcutoatributo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nombres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('numero', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Nombre',
                'verbose_name_plural': 'Nombres',
                'db_table': 'nombres',
            },
        ),
    ]
