from django.db import models


class Student(models.Model):
    user = models.ForeignKey('auth.User')

    rol = models.CharField(max_length=20)
