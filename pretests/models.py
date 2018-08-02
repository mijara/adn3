# coding=utf-8
from django.db import models


class Pretest(models.Model):
    # related course.
    course = models.ForeignKey('courses.Course')

    name = models.CharField(max_length=128, verbose_name=u'Nombre')

    start_session = models.ForeignKey('classes.Session', related_name='start_session',
                                      verbose_name='Sesión Inicio')

    end_session = models.ForeignKey('classes.Session', related_name='end_session',
                                    verbose_name='Sesión Entrega')

    percentage = models.IntegerField(default=0, verbose_name='Porcentaje Nota')

    show_grade = models.BooleanField(default=False, verbose_name='Mostrar calificación',
                                     help_text='Mostrará la calificación al estudiante posterior a la revisión.')

    online = models.BooleanField(default=False, verbose_name='Entrega Online',
                                 help_text='Permitirá al estudiante enviar un '
                                           'archivo a través del sistema, para que el '
                                           'encargado posteriormente lo descargue y evalúe.')

    def __str__(self):
        return self.name + ' - ' + self.course.__str__()

    @models.permalink
    def get_absolute_url(self):
        return 'pretests:pretest_detail', [self.course.pk, self.pk]

    @models.permalink
    def get_update_url(self):
        return 'pretests:pretest_update', [self.course.pk, self.pk]

    @models.permalink
    def get_delete_url(self):
        return 'pretests:pretest_delete', [self.course.pk, self.pk]

    def get_submitted_pretests(self):
        pretests = self.pretestupload_set.all()
        reviewed = 0
        for pretest in self.pretestupload_set.all():
            if pretest.qualification is not None:
                reviewed  += 1
        if len(pretests):
            return [pretests, len(pretests), reviewed, len(pretests) - reviewed]
        else:
            return None


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
        return 'pretests:pretestfile_delete', [self.pretest.course.pk,
                                               self.pretest.pk, self.pk]


class PretestUpload(models.Model):
    software = models.ForeignKey('misc.Software', verbose_name='Software', null=True, blank=True)

    pretest = models.ForeignKey(Pretest, verbose_name='Preinforme')

    student = models.ForeignKey('registration.Student', verbose_name='Estudiante')

    file = models.FileField(verbose_name='Archivo', null=True, blank=True)

    qualification = models.IntegerField(verbose_name='Calificación', null=True, blank=True)

    feedback = models.TextField(verbose_name='Comentario', null=True, blank=True)

    def __str__(self):
        return self.pretest.name

    def get_download_url(self):
        return self.file.url

    @models.permalink
    def get_review_url(self):
        return 'pretests:pretest_review', [self.pretest.course.pk, self.pretest.pk, self.pk]
