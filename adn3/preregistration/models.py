from __future__ import unicode_literals

from django.db import models


class PreRegistration(models.Model):
    user = models.ForeignKey('auth.User')

    first_preference = models.ForeignKey('courses.Agenda', related_name='first')
    second_preference = models.ForeignKey('courses.Agenda', related_name='second')
    third_preference = models.ForeignKey('courses.Agenda', related_name='third')

    def __unicode__(self):
        return self.user
