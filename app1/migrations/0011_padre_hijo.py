# Generated by Django 5.1.1 on 2024-10-06 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_progenitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Padres',
            },
        ),
        migrations.CreateModel(
            name='Hijo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('padre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.padre')),
            ],
            options={
                'verbose_name_plural': 'Hijos',
            },
        ),
    ]
