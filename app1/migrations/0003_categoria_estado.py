# Generated by Django 5.1.1 on 2024-10-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_categoria_activo_categoria_fecha_crea_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8),
        ),
    ]
