# coding=utf-8
from django.db import models
from django.urls import reverse_lazy

from adn3.choices import make_days_blocks


class FlyIn(models.Model):
    course = models.ForeignKey('courses.Course')
    software = models.ForeignKey('misc.Software')

    first_name = models.CharField(max_length=128, verbose_name='Nombre')
    last_names = models.CharField(max_length=128, verbose_name='Apellidos')

    rol = models.CharField(max_length=20, verbose_name='Rol USM')
    usm_priority = models.FloatField(verbose_name='Prioridad')
    parallel = models.IntegerField()

    previous_experience = models.BooleanField()

    first_preference = models.CharField(
        choices=make_days_blocks(),
        max_length=32,
        verbose_name='Primera Preferencia')

    second_preference = models.CharField(
        choices=make_days_blocks(),
        max_length=32,
        verbose_name='Segunda Preferencia', blank=True, null=True)

    third_preference = models.CharField(
        choices=make_days_blocks(),
        max_length=32,
        verbose_name='Tercera Preferencia', blank=True, null=True)

    fourth_preference = models.CharField(
        choices=make_days_blocks(),
        max_length=32,
        verbose_name='Cuarta Preferencia', blank=True, null=True)

    fifth_preference = models.CharField(
        choices=make_days_blocks(),
        max_length=32,
        verbose_name='Quinta Preferencia', blank=True, null=True)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_names

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse_lazy('flyins:preregistration_detail',
                            args=[self.pk])
