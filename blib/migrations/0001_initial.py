# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('li_ISBN', models.CharField(max_length=13)),
                ('li_Titulo', models.CharField(max_length=20)),
                ('li_Autor', models.CharField(max_length=20)),
                ('li_Editorial', models.CharField(max_length=20)),
                ('li_Pais', models.CharField(max_length=15)),
                ('li_anio', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('pres_FechaPrestamo', models.DateTimeField(default=django.utils.timezone.now)),
                ('pres_FechaDevolucionPropuesta', models.DateTimeField()),
                ('pres_FechaDevolucionReal', models.DateTimeField()),
                ('pres_Libros', models.ForeignKey(to='blib.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('us_Nombre', models.CharField(max_length=20)),
                ('us_DPI', models.CharField(max_length=13)),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='pres_Usuario',
            field=models.ForeignKey(to='blib.Usuario'),
        ),
    ]
