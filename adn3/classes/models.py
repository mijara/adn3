# coding=utf-8
from django.db import models
from adn3.choices import *


class Class(models.Model):
    # related course.
    course = models.ForeignKey('courses.Course')

    # name of the session.
    name = models.CharField(max_length=128, verbose_name=u'Nombre')

    # number of session.
    number = models.IntegerField(choices=make_session_numbers(), verbose_name=u'Número')

    # start date of the classes.
    start_date = models.DateField(verbose_name=u'Fecha inicio')

    # end date of the classes.
    end_date = models.DateField(verbose_name=u'Fecha término')

    # use for ordering.
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('number',)

    def __unicode__(self):
        return self.name

    def duration(self):
        return (self.end_date - self.start_date).days
