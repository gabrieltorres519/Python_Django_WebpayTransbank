# Generated by Django 3.0.5 on 2024-02-05 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_tracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.PositiveIntegerField(default=0),
        ),
    ]