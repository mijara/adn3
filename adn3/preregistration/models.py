# coding=utf-8
from django.db import models


class PreRegistration(models.Model):
    course = models.ForeignKey('courses.Course')

    first_name = models.CharField(max_length=256, verbose_name=u'Nombre')
    last_names = models.CharField(max_length=256, verbose_name=u'Apellidos')

    usm_rol = models.CharField(max_length=12, verbose_name='Rol USM')

    usm_priority = models.IntegerField(verbose_name='Prioridad USM')
    psu_score = models.IntegerField(verbose_name='Puntaje PSU',
                                    help_text=u'Para alumnos de primer año',
                                    null=True, blank=True)

    first_preference = models.ForeignKey(
        'courses.Agenda',
        related_name='first',
        verbose_name='Primera Preferencia')

    second_preference = models.ForeignKey(
        'courses.Agenda',
        related_name='second',
        verbose_name='Segunda Preferencia', blank=True, null=True)

    third_preference = models.ForeignKey(
        'courses.Agenda',
        related_name='third',
        verbose_name='Tercera Preferencia', blank=True, null=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_names
