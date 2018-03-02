# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-04 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0004_auto_20170925_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=32, verbose_name='1.- ¿Ud. había usado antes algún software matemático o estadístico?')),
                ('second', models.IntegerField(verbose_name='2.- ¿A cuantas sesiones de laboratorio computacional asistió?')),
                ('third', models.CharField(choices=[('Muy complicado', 'Muy complicado'), ('Complicado', 'Complicado'), ('Amigable', 'Amigable'), ('Muy Amigable', 'Muy Amigable')], max_length=32, verbose_name='3.- El material de instrucción le pareció :')),
                ('fourth', models.CharField(choices=[('Inadecuado', 'Inadecuado'), ('Poco adecuado', 'Poco adecuado'), ('Adecuado', 'Adecuado'), ('Muy adecuado', 'Muy adecuado')], max_length=32, verbose_name='4.- La presentación del material de instrucción le pareció:')),
                ('fifth', models.CharField(choices=[('Muy atrasado', 'Muy atrasado'), ('Atrasado', 'Atrasado'), ('A Tiempo', 'A Tiempo'), ('Adelantado', 'Adelantado')], max_length=32, verbose_name='5.- El material de instrucción respecto de las clases teóricas fue:')),
                ('sixth', models.CharField(choices=[('Escasa', 'Escasa'), ('Buena', 'Buena'), ('Muy Buena', 'Muy Buena')], max_length=32, verbose_name='6.- La ayuda del ayudante de laboratorio le pareció:')),
                ('seventh', models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=32, verbose_name='7.- ¿Fueron atendidas a tiempo sus consultas e inquietudes por el ayudante coordinador?')),
                ('eighth', models.CharField(choices=[('Muy corto', 'Muy corto'), ('Corto', 'Corto'), ('Normal', 'Normal'), ('Excesivo', 'Excesivo')], max_length=32, verbose_name='8.- El tiempo disponible en cada sesión es:')),
                ('ninth', models.CharField(choices=[('Incómodas', 'Incómodas'), ('Cómodas', 'Cómodas'), ('Muy Cómodas', 'Muy Cómodas')], max_length=32, verbose_name='9.- Las instalaciones del laboratorio le parecen:')),
                ('tenth', models.CharField(choices=[('Una', 'Una'), ('Dos', 'Dos'), ('Una Quincenal', 'Una Quincenal')], max_length=32, verbose_name='10.- ¿Cuantas sesiones a la semana considera necesarias?')),
                ('eleventh', models.CharField(choices=[('Inútiles', 'Inútiles'), ('Poco útiles', 'Poco útiles'), ('Útiles', 'Útiles'), ('Muy Útiles', 'Muy Útiles')], max_length=32, verbose_name='11.- Los preinformes (para entender la sesión) son:')),
                ('twelfth', models.CharField(choices=[('Muy difíciles', 'Muy difíciles'), ('Difíciles', 'Difíciles'), ('Adecuados', 'Adecuados'), ('Fáciles', 'Fáciles')], max_length=32, verbose_name='12.- Los controles le parecieron:')),
                ('thirteenth', models.CharField(choices=[('Poco adecuado', 'Poco adecuado'), ('Adecuado', 'Adecuado'), ('Inadecuado', 'Inadecuado')], max_length=32, verbose_name='13.- El “sistema Aula” para la sesión le parece:')),
                ('fourteenth', models.CharField(choices=[('Muy complicado', 'Muy complicado'), ('Complicado', 'Complicado'), ('Bueno', 'Bueno'), ('Muy Bueno', 'Muy Bueno')], max_length=32, verbose_name='14.- El “sistema Aula” para controles le parece:')),
                ('fifteenth', models.CharField(choices=[('Inútil', 'Inútil'), ('Poco Útil', 'Poco Útil'), ('Útil', 'Útil'), ('Muy Útil', 'Muy Útil')], max_length=32, verbose_name='15.- Globalmente la experiencia del laboratorio fue:')),
                ('sixteenth', models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=32, verbose_name='16.- Usted quisiera experimentar por su propia cuenta con el software en horarios distintos al de la sesión:')),
                ('seventeenth', models.CharField(choices=[('Sólo', 'Sólo'), ('Con Otro Alumno', 'Con Otro Alumno'), ('Me da Igual', 'Me da Igual')], max_length=32, verbose_name='17.- Usted hubiese preferido trabajar en cada sesión: ')),
                ('eighteenth', models.TextField(verbose_name='18.- Comentarios y sugerencias:')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Curso')),
            ],
        ),
    ]