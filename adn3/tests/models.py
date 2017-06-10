# coding=utf-8
from django.core.urlresolvers import reverse_lazy
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from django.db import models

from django.utils import timezone


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

    create_date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                       verbose_name=u'Fecha de creación')

    show_grade = models.BooleanField(default=True,
                                     verbose_name=u'Mostrar nota')

    active = models.BooleanField(default=True, verbose_name=u'Activo')

    percentage = models.IntegerField(verbose_name=u'Porcentaje')

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'tests:test_detail', [self.course.pk, self.pk]

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

    file = models.FileField(upload_to='tests/', blank=True)

    students = models.ManyToManyField('auth.User', verbose_name=u'Estudiante', blank=True,
                                      related_name=u'students', through='StudentsAnswers')

    class Meta:
        verbose_name = 'Forma'
        verbose_name_plural = 'Formas'

    def __str__(self):
        return self.test.name

    @models.permalink
    def get_absolute_url(self):
        return 'tests:version_detail', [self.test.course.pk, self.test.pk, self.pk]

    @models.permalink
    def get_delete_url(self):
        return 'tests:version_delete', [self.test.course.pk, self.test.pk, self.pk]


class StudentsAnswers(models.Model):
    version = models.ForeignKey('Version', verbose_name=u'Forma')

    student = models.ForeignKey('auth.User', verbose_name=u'Estudiante')

    started_at = models.DateTimeField(auto_now_add=True, auto_now=False,
                                      verbose_name=u'Fecha de inicio')

    last_update = models.DateTimeField(auto_now=False, verbose_name=u'Última actualización', null=True, blank=True)

    submitted = models.BooleanField(verbose_name='Enviado', default=False)

    document = models.FileField(null=True, blank=True)

    # Return the answers status
    # 1: In progress
    # 2: It's over
    def get_status(self):
        finish_time = self.started_at + timezone.timedelta(minutes=self.version.test.timeout + 0.2)

        if finish_time < timezone.now() or self.submitted:
            return 2
        else:
            return 1

    def get_time_left(self):
        finish_time = self.started_at + timezone.timedelta(minutes=self.version.test.timeout)
        if finish_time > timezone.now():
            left = finish_time - timezone.now()
            return left.total_seconds() / 60
        return 0

    def get_time_elapsed(self):
        return self.version.test.timeout - self.get_time_left()

    def get_document_url(self):
        return self.document.url


class Question(models.Model):
    version = models.ForeignKey('Version', verbose_name=u'Forma')

    text = models.TextField(verbose_name=u'Enunciado')

    score = models.IntegerField(
        default=100,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        verbose_name=u'Puntaje')

    html = models.TextField(verbose_name=u'html')

    def __str__(self):
        return self.text[:25]


class TextQuestion(Question):
    def get_update_url(self):
        return reverse_lazy('tests:textquestion_update',
                            args=[self.version.test.course.pk, self.version.test.pk,
                                  self.version.pk, self.pk])

    def get_delete_url(self):
        return reverse_lazy('tests:textquestion_delete',
                            args=[self.version.test.course.pk, self.version.test.pk,
                                  self.version.pk, self.pk])


class NumericalQuestion(Question):
    top_limit = models.FloatField(verbose_name=u'Límite Superior')
    bottom_limit = models.FloatField(verbose_name=u'Límite Inferior')

    def get_update_url(self):
        return reverse_lazy('tests:numericalquestion_update',
                            args=[self.version.test.course.pk, self.version.test.pk,
                                  self.version.pk, self.pk])


class ChoiceQuestion(Question):
    def get_update_url(self):
        return reverse_lazy('tests:choicequestion_update',
                            args=[self.version.test.course.pk, self.version.test.pk,
                                  self.version.pk, self.pk])


class Answer(models.Model):
    student = models.ForeignKey('auth.User', verbose_name=u'Estudiante')
    question = models.ForeignKey('Question', verbose_name=u'Pregunta')

    def __str__(self):
        return self.student.username


class TextAnswer(Answer):
    text = models.TextField(verbose_name=u'Texto', null=True, blank=True)


class NumericalAnswer(Answer):
    number = models.FloatField(verbose_name=u'Número', null=True, blank=True)


class ChoiceAnswer(Answer):
    alternative = models.ForeignKey('Alternative', verbose_name=u'Alternativa', null=True, blank=True)


class Alternative(models.Model):
    question = models.ForeignKey('ChoiceQuestion', verbose_name=u'Pregunta')

    index = models.IntegerField(verbose_name=u'Índice')
    text = models.TextField(verbose_name=u'Texto')
    correct = models.BooleanField(default=False, verbose_name=u'Es correcta')

    def __str__(self):
        return self.text

    def index_as_name(self):
        return 'ABCDE'[self.index - 1]

    class Meta:
        ordering = ('index',)


@receiver(pre_delete, sender=StudentsAnswers)
def pre_delete(sender, instance, **kwargs):
    for question in instance.version.question_set.all():
        try:
            Answer.objects.get(student=instance.student, question=question).delete()
        except:
            pass
