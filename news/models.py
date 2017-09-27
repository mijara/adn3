# coding=utf-8
from django.db import models


class New(models.Model):
    course = models.ForeignKey('courses.Course', verbose_name=u'Curso')

    title = models.CharField(max_length=512, verbose_name=u'Título')

    body = models.TextField(verbose_name=u'Cuerpo')

    html = models.TextField(verbose_name=u'Html')

    owner = models.ForeignKey('auth.User')

    create_date = models.DateTimeField(auto_now_add=True)

    update_date = models.DateTimeField(auto_now=True)

    public = models.BooleanField(default=False, verbose_name=u'Público',
                                 help_text=u'Si es público, además, se mostrará a usuarios '
                                           u'externos a la universidad.')

    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'news:new_detail', [self.course.pk, self.pk]

    @models.permalink
    def get_update_url(self):
        return 'news:new_update', [self.course.pk, self.pk]

    @models.permalink
    def get_delete_url(self):
        return 'news:new_delete', [self.course.pk, self.pk]
