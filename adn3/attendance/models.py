from django.db import models


class Attendance(models.Model):
    NO_ATTENDED = 0
    ATTENDED = 1
    JUSTIFIED = 2

    session = models.ForeignKey('classes.Session')
    agenda = models.ForeignKey('courses.Agenda')
    user = models.ForeignKey('auth.User')

    attended = models.IntegerField(choices=[
        (NO_ATTENDED, 'No'),
        (ATTENDED, 'Si'),
        (JUSTIFIED, 'Justificado'),
    ])

    class Meta:
        unique_together = ('session', 'agenda', 'user')

    def __unicode__(self):
        return u'[%s] %s: %s' % (self.agenda, self.session, self.user.get_full_name())
