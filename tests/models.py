# coding=utf-8
from django.core.urlresolvers import reverse_lazy
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from django.db import models

from django.utils import timezone

from attendance.models import Attendance
from courses.models import Agenda


class Test(models.Model):
    course = models.ForeignKey('courses.Course', verbose_name=u'Curso')

    session = models.ForeignKey('classes.Session', verbose_name=u'Sesión')

    owner = models.ForeignKey('auth.User', verbose_name=u'Dueño')

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

    percentage = models.IntegerField(verbose_name=u'Porcentaje')

    class Meta:
        ordering = ('create_date',)

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

    def get_submitted_tests(self):
        tests = []
        reviewed = 0
        for version in self.version_set.all():
            for answer in version.studentsanswers_set.all():
                if answer.get_status() == 2:
                    tests.append(answer)
                    if answer.qualification is not None:
                        reviewed += 1
        if len(tests):
            return [tests, len(tests), reviewed, len(tests) - reviewed]
        else:
            return None

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            for agenda in self.course.agenda_set.all():
                AgendaTest.objects.create(agenda=agenda, test=self)


    def is_student_allowed(self, user):
        agenda = Agenda.objects.filter(
            course=self.course, inscriptions__in=[user]
        ).get()

        attendance = Attendance.objects.filter(
            session=self.session, agenda=agenda, user=user)

        if not attendance.exists():
            return False
        elif attendance.get().attended not in (Attendance.ATTENDED, Attendance.JUSTIFIED):
            return False

        return True


class AgendaTest(models.Model):
    agenda = models.ForeignKey('courses.Agenda')

    test = models.ForeignKey('tests.Test')

    active = models.BooleanField(default=False)


class Version(models.Model):
    test = models.ForeignKey('Test', verbose_name='Control')

    create_date = models.DateTimeField(auto_now_add=True)

    file = models.FileField(upload_to='tests/', blank=True)

    students = models.ManyToManyField(
        'auth.User',
        verbose_name=u'Estudiante',
        blank=True,
        related_name=u'registration',
        through='StudentsAnswers')

    class Meta:
        verbose_name = 'Forma'
        verbose_name_plural = 'Formas'
        ordering = ('create_date',)

    def __str__(self):
        return "Forma %s - %s" % (self.get_letter(), self.test.name)

    @models.permalink
    def get_absolute_url(self):
        return 'tests:version_detail', [self.test.course.pk, self.test.pk,
                                        self.pk]

    @models.permalink
    def get_delete_url(self):
        return 'tests:version_delete', [self.test.course.pk, self.test.pk,
                                        self.pk]

    @models.permalink
    def get_duplicate_url(self):
        return 'tests:version_duplicate', [self.test.course.pk, self.test.pk,
                                           self.pk]

    def get_letter(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        versions = Version.objects.filter(test=self.test)

        for i, version in enumerate(versions):
            if version == self:
                return letters[i]
        return "A"


class StudentsAnswers(models.Model):
    version = models.ForeignKey('Version', verbose_name=u'Forma')

    student = models.ForeignKey('auth.User', verbose_name=u'Estudiante')

    started_at = models.DateTimeField(auto_now_add=True, auto_now=False,
                                      verbose_name=u'Fecha de inicio')

    last_update = models.DateTimeField(
        auto_now=False,
        verbose_name=u'Última actualización',
        null=True,
        blank=True)

    submitted = models.BooleanField(verbose_name='Enviado', default=False)

    document = models.FileField(null=True, blank=True)

    qualification = models.IntegerField(null=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.version.__str__()

    # Return the answers status
    # 1: In progress
    # 2: It's over
    # There is a delta of 5 minutes
    def get_status(self):
        finish_time = self.started_at + timezone.timedelta(
            minutes=self.version.test.timeout + 5)

        if finish_time < timezone.now() or self.submitted:
            return 2
        else:
            return 1

    def get_time_left(self):
        finish_time = self.started_at + timezone.timedelta(
            minutes=self.version.test.timeout)
        if finish_time > timezone.now():
            left = finish_time - timezone.now()
            return left.total_seconds() / 60
        return 0

    def get_time_elapsed(self):
        return self.version.test.timeout - self.get_time_left()

    def get_document_url(self):
        return self.document.url

    def get_student_agenda(self):
        course = self.version.test.course
        for agenda in self.student.inscriptions.filter(course=course):
            return agenda
        return None

    @models.permalink
    def get_review_url(self):
        return 'tests:test_review', [self.version.test.course.pk,
                                     self.version.test.pk, self.pk]


class Question(models.Model):
    version = models.ForeignKey('Version', verbose_name=u'Forma')

    text = models.TextField(verbose_name=u'Enunciado')

    score = models.IntegerField(
        default=100,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        verbose_name=u'Puntaje')

    html = models.TextField(verbose_name=u'html')

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.text[:25]

    def get_correct_incorrect_answers(self):
        correct = len(self.answer_set.filter(correct=True))
        incorrect = len(self.answer_set.filter(correct=False))
        return correct, incorrect


class TextQuestion(Question):
    def get_update_url(self):
        return reverse_lazy('tests:textquestion_update',
                            args=[self.version.test.course.pk,
                                  self.version.test.pk,
                                  self.version.pk, self.pk])

    def get_delete_url(self):
        return reverse_lazy('tests:textquestion_delete',
                            args=[self.version.test.course.pk,
                                  self.version.test.pk,
                                  self.version.pk, self.pk])


class NumericalQuestion(Question):
    top_limit = models.FloatField(verbose_name=u'Límite Superior')
    bottom_limit = models.FloatField(verbose_name=u'Límite Inferior')

    def get_update_url(self):
        return reverse_lazy('tests:numericalquestion_update',
                            args=[self.version.test.course.pk,
                                  self.version.test.pk,
                                  self.version.pk, self.pk])


class ChoiceQuestion(Question):
    def get_update_url(self):
        return reverse_lazy('tests:choicequestion_update',
                            args=[self.version.test.course.pk,
                                  self.version.test.pk,
                                  self.version.pk, self.pk])


class Answer(models.Model):
    student = models.ForeignKey('auth.User', verbose_name=u'Estudiante')
    question = models.ForeignKey('Question', verbose_name=u'Pregunta')
    correct = models.NullBooleanField(verbose_name=u'Es correcta')

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.student.username


class TextAnswer(Answer):
    text = models.TextField(verbose_name=u'Texto', null=True, blank=True)


class NumericalAnswer(Answer):
    number = models.FloatField(verbose_name=u'Número', null=True, blank=True)

    def is_correct(self):
        if not self.number: return False
        return self.question.numericalquestion.top_limit >= self.number >= self.question.numericalquestion.bottom_limit


class ChoiceAnswer(Answer):
    alternative = models.ForeignKey('Alternative', verbose_name=u'Alternativa',
                                    null=True, blank=True)


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
            Answer.objects.get(student=instance.student,
                               question=question).delete()
        except:
            pass
