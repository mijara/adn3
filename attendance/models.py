from django.db import models


class Attendance(models.Model):
    """
    Attendance of a user to certain session and agenda.
    """
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
    ], default=NO_ATTENDED)

    class Meta:
        unique_together = ('session', 'agenda', 'user')

    def __str__(self):
        return u'[%s] %s: %s' % (self.agenda, self.session, self.user.get_full_name())
