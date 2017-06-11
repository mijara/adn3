# coding=utf-8
from django.db import models
from django.urls import reverse_lazy

from adn3 import choices


class PreRegistration(models.Model):
    course = models.ForeignKey('courses.Course')
    student = models.ForeignKey('students.Student')

    # TODO: CharField should have convenient choices for each day-block.

    first_preference = models.CharField(
        max_length=32,
        verbose_name='Primera Preferencia')

    second_preference = models.CharField(
        max_length=32,
        verbose_name='Segunda Preferencia', blank=True, null=True)

    third_preference = models.CharField(
        max_length=32,
        verbose_name='Tercera Preferencia', blank=True, null=True)

    fourth_preference = models.CharField(
        max_length=32,
        verbose_name='Cuarta Preferencia', blank=True, null=True)

    fifth_preference = models.CharField(
        max_length=32,
        verbose_name='Quinta Preferencia', blank=True, null=True)

    def __str__(self):
        return str(self.student)

    def get_absolute_url(self):
        return reverse_lazy('preregistrations:preregistration_detail',
                            args=[self.pk])
