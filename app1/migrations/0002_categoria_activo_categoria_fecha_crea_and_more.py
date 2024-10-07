# Generated by Django 5.1.1 on 2024-10-06 18:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='categoria',
            name='fecha_crea',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoria',
            name='fecha_modifica',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
