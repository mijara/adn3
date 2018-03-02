from django.db import models


class SuperTeacher(models.Model):
    """
    A super teacher is a special type of teacher which has special attributes.
    """

    # assigned super teacher.
    teacher = models.ForeignKey('auth.User')

    # campus on which this teacher can manage all courses.
    campus = models.ForeignKey('courses.Campus', null=True, blank=True)
