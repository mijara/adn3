# coding=utf-8
from django.db import models


class Pretest(models.Model):
    # related course.
    course = models.ForeignKey('courses.Course')

    name = models.CharField(max_length=128, verbose_name=u'Nombre')

    start_session = models.ForeignKey('classes.Session', related_name='start_session',
                                      verbose_name=u'Sesión Inicio')

    end_session = models.ForeignKey('classes.Session', related_name='end_session',
                                    verbose_name=u'Sesión Entrega')

    percentage = models.FloatField(default=0, verbose_name=u'Porcentaje')

    show_grade = models.BooleanField(default=False, verbose_name=u'Mostrar calificación')

    def __unicode__(self):
        return self.name


class PretestFile(models.Model):
    pretest = models.ForeignKey('Pretest')

    name = models.CharField(max_length=128)

    file = models.FileField()

    def __unicode__(self):
        return self.name
