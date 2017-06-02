from django.db import models
import uuid

from django.urls import reverse_lazy


class Student(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Usuario')

    rol = models.CharField(max_length=20, verbose_name='Rol USM')

    usm_priority = models.IntegerField(verbose_name='Prioridad')


class ReserveAttempt(models.Model):
    """
    Reserve Attempt describes an attempt to use an email account for an user.
    The user should validate via email that this is his account in order to proceed.
    """

    email = models.EmailField()

    secret = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        # generate secret.
        self.secret = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('students:reserveattempt_detail', args=[self.pk])

    def __str__(self):
        return self.email
