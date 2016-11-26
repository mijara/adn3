# coding=utf-8
from django.core.urlresolvers import reverse_lazy
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Test(models.Model):
    course = models.ForeignKey('courses.Course', verbose_name=u'Curso')
    session = models.ForeignKey('classes.Session', verbose_name=u'Sesión')
    owner = models.ForeignKey('auth.User', verbose_name=u'Dueño')
    software = models.ForeignKey('misc.Software', verbose_name=u'Software')

    name = models.CharField(max_length=128, verbose_name=u'Nombre')

    timeout = models.IntegerField(choices=[
        (15, u'15 minutos'),
        (30, u'30 minutos'),
        (45, u'45 minutos'),
        (60, u'1 hora'),
        (75, u'1 hora 15 minutos'),
        (90, u'1 hora 30 minutos'),
        (105, u'1 hora 45 minutos'),
    ], verbose_name=u'Duración')

    create_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u'Fecha de creación')

    show_grade = models.BooleanField(default=True, verbose_name=u'Mostrar nota')

    active = models.BooleanField(default=True, verbose_name=u'Activo')

    percentage = models.IntegerField(verbose_name=u'Porcentaje')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'tests:test_detail', [self.pk]

    @models.permalink
    def get_update_url(self):
        return 'tests:test_update', [self.course.pk, self.pk]

    @models.permalink
    def get_delete_url(self):
        return 'tests:test_delete', [self.course.pk, self.pk]


class Version(models.Model):
    test = models.ForeignKey('Test', verbose_name='Control')

    create_date = models.DateTimeField(auto_now_add=True)

    index = models.IntegerField()

    class Meta:
        verbose_name = 'Forma'
        verbose_name_plural = 'Formas'

    def __unicode__(self):
        return self.test.name

    @models.permalink
    def get_absolute_url(self):
        return 'tests:version_detail', [self.pk]

    @models.permalink
    def get_delete_url(self):
        return 'tests:version_delete', [self.test.pk, self.pk]


class Question(models.Model):
    version = models.ForeignKey('Version', verbose_name='Forma')

    text = models.TextField(verbose_name=u'Enunciado')

    score = models.IntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)],
                                verbose_name=u'Puntaje')

    def __unicode__(self):
        return self.text[:25]


class ChoiceQuestion(Question):
    pass


class Alternative(models.Model):
    question = models.ForeignKey('ChoiceQuestion')

    index = models.IntegerField(verbose_name=u'Índice')
    text = models.TextField(verbose_name=u'Texto')
    correct = models.BooleanField(default=False, verbose_name=u'Es correcta')

    def __unicode__(self):
        return self.text

    def index_as_name(self):
        return 'ABCDE'[self.index - 1]

    class Meta:
        ordering = ('index',)
