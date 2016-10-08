# coding=utf-8
from django.db import models
from adn3.choices import *


class Session(models.Model):
    PRIVATE = 0
    PUBLIC = 1

    REGULAR = 0
    TEST = 1
    RECUPERATIVE = 2

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

    # if this session is private or public.
    state = models.IntegerField(default=PRIVATE, choices=[
        (PRIVATE, 'Privada'),
        (PUBLIC, 'Pública'),
    ], verbose_name='Estado')

    # what kind of session is this, regular, recuperative or test.
    session_type = models.IntegerField(default=REGULAR, choices=[
        (REGULAR, 'Regular'),
        (TEST, 'Prueba'),
        (RECUPERATIVE, 'Recuperativa'),
    ], verbose_name='Tipo')

    # use for ordering.
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('number',)

    def __unicode__(self):
        return self.name

    def duration(self):
        return (self.end_date - self.start_date).days
