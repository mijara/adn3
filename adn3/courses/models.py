# coding=utf-8
from django.db import models
from adn3.choices import *


class Campus(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Campuses'

    def __unicode__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=32)
    seats = models.IntegerField()

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

    # Added for statistics.
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s %d-%d' % (self.name, self.campus.name, self.year, self.semester)


class Agenda(models.Model):
    day = models.IntegerField(choices=make_days())
    room = models.ForeignKey(Room)
    course = models.ForeignKey(Course)
    block = models.IntegerField(choices=make_blocks())

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.course, self.get_block_display(), self.room.name)
