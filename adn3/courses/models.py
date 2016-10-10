# coding=utf-8
from django.db import models
from adn3.choices import *


class Campus(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'Nombre')

    class Meta:
        verbose_name_plural = 'Campuses'

    def __unicode__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'Nombre')
    code = models.CharField(max_length=32, verbose_name=u'Código')
    seats = models.IntegerField(verbose_name=u'Asientos')

    def __unicode__(self):
        return self.name


class Course(models.Model):
    """
    A simple course.
    """
    name = models.CharField(max_length=256, verbose_name=u'Nombre')
    code = models.CharField(max_length=16, verbose_name=u'Sigla')
    campus = models.ForeignKey(Campus)

    # Temporal fields.
    semester = models.IntegerField(choices=[(1, 1), (2, 2)], verbose_name=u'Semestre')
    year = models.IntegerField(choices=make_years(), verbose_name=u'Año')

    # state of the course.
    status = models.BooleanField(default=True, verbose_name=u'Estado')

    teachers = models.ManyToManyField('auth.User', through='CourseTeacher', blank=True, verbose_name='Profesores')

    # Added for statistics.
    create_date = models.DateTimeField(auto_now_add=True)

    def count_inscriptions(self):
        count = 0

        for agenda in self.agenda_set.all():
            count += agenda.inscriptions.count()

        return count

    def __unicode__(self):
        return u'%s - %s %d-%d' % (self.name, self.campus.name, self.year, self.semester)


class Agenda(models.Model):
    day = models.IntegerField(choices=make_days(), verbose_name=u'Día')
    room = models.ForeignKey(Room, verbose_name=u'Sala')
    course = models.ForeignKey(Course, verbose_name=u'Curso')
    block = models.IntegerField(choices=make_blocks(), verbose_name=u'Bloque')

    inscriptions = models.ManyToManyField('auth.User', verbose_name=u'Inscritos', blank=True,
                                          related_name='inscriptions')

    assistants = models.ManyToManyField('auth.User', verbose_name=u'Ayudantes', blank=True,
                                        related_name='assistants')

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.course, self.get_block_display(), self.room.name)


class CourseTeacher(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Profesor')
    course = models.ForeignKey('Course', verbose_name='Curso')
    coordinates = models.BooleanField(verbose_name=u'Coordinador')

    def __unicode__(self):
        return self.user.username
