# coding=utf-8
from django.db import models


class New(models.Model):
    course = models.ForeignKey('courses.Course', verbose_name=u'Curso')
    title = models.CharField(max_length=512, verbose_name=u'Título')
    body = models.TextField(verbose_name=u'Cuerpo')
    owner = models.ForeignKey('auth.User')

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'[%s] %s' % (self.course, self.title)
