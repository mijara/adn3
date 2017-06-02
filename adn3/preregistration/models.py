# coding=utf-8
from django.db import models
from django.urls import reverse_lazy


class PreRegistration(models.Model):
    course = models.ForeignKey('courses.Course')
    student = models.ForeignKey('students.Student')

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

    def __str__(self):
        return str(self.student)

    def get_absolute_url(self):
        return reverse_lazy('preregistrations:preregistration_detail',
                            args=[self.pk])
