# coding=utf-8
from django.db import models
from django.urls import reverse_lazy

from adn3 import choices
from adn3.choices import make_days_blocks


class PreRegistration(models.Model):
    course = models.ForeignKey('courses.Course')
    student = models.ForeignKey('students.Student')

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

    def __str__(self):
        return str(self.student)

    def get_absolute_url(self):
        return reverse_lazy('preregistrations:preregistration_detail',
                            args=[self.pk])

    def get_delete_url(self):
        return reverse_lazy('preregistrations:preregistration_delete',
                            args=[self.pk])
