from django.db import models
import uuid

from django.urls import reverse_lazy

from tests.models import Test


class Student(models.Model):
    user = models.OneToOneField('auth.User', verbose_name='Usuario')

    rol = models.CharField(max_length=20, verbose_name='Rol USM')

    usm_priority = models.IntegerField(verbose_name='Prioridad', null=True, blank=True)

    campus = models.ForeignKey('courses.Campus')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_absolute_url(self):
        return reverse_lazy('registration:student_detail')

    def get_grades_for_course(self, course):
        for test in course.test_set.all():
            version = test.version_set.filter(students__student=self)

            if not version.exists():
                yield test.name, None

            else:
                version = version.first()
                answers = version.studentsanswers_set.filter(student=self.user)

                if not answers.exists():
                    yield test.name, None
                else:
                    answers = answers.first()
                    yield test.name, answers.qualification


class Ticket(models.Model):
    """
    Ticket describes an attempt to use an email account for an user.
    The user should validate via email that this is his account in order to proceed.
    """
    email = models.EmailField()

    secret = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        # generate secret.
        self.secret = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('registration:ticket_detail', args=[self.pk])

    def __str__(self):
        return self.email
