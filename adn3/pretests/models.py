# coding=utf-8
from django.db import models


class Pretest(models.Model):
    # related course.
    course = models.ForeignKey('courses.Course')

    name = models.CharField(max_length=128, verbose_name=u'Nombre')

    start_session = models.ForeignKey('classes.Session', related_name='start_session',
                                      verbose_name=u'Sesión Inicio')

    end_session = models.ForeignKey('classes.Session', related_name='end_session',
                                    verbose_name=u'Sesión Entrega')

    percentage = models.IntegerField(default=0, verbose_name=u'Porcentaje')

    show_grade = models.BooleanField(default=False, verbose_name=u'Mostrar calificación')

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'pretests:pretest_detail', [self.pk]

    @models.permalink
    def get_update_url(self):
        return 'pretests:pretest_update', [self.course.pk, self.pk]

    @models.permalink
    def get_delete_url(self):
        return 'pretests:pretest_delete', [self.course.pk, self.pk]


class PretestFile(models.Model):
    pretest = models.ForeignKey('Pretest')

    name = models.CharField(max_length=128)

    file = models.FileField()

    def __str__(self):
        return self.name

    def get_download_url(self):
        return self.file.url

    @models.permalink
    def get_delete_url(self):
        return 'pretests:pretestfile_delete', [self.pk]


class PretestUpload(models.Model):
    software = models.ForeignKey('misc.Software', verbose_name='Software')

    pretest = models.ForeignKey(Pretest, verbose_name='Preinforme')

    student = models.ForeignKey('students.Student', verbose_name='Estudiante')

    file = models.FileField(verbose_name='Archivo')
