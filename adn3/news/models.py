from django.db import models


class New(models.Model):
    course = models.ForeignKey('courses.Course')
    title = models.CharField(max_length=512)
    content = models.TextField()

    def __unicode__(self):
        return u'[%s] %s' % (self.course, self.title)
