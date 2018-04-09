# coding=utf-8
from django.db import models
from adn3.choices import *
from adn3.services import get_year_semester
import random


class Campus(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'Nombre')

    class Meta:
        verbose_name_plural = 'Campus'

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'Nombre')

    code = models.CharField(max_length=32, verbose_name=u'Código')

    seats = models.IntegerField(verbose_name=u'Asientos')

    campus = models.ForeignKey(Campus, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.name, self.campus.name)


class Course(models.Model):
    """
    A simple course.
    """
    name = models.CharField(max_length=256, verbose_name=u'Nombre')
    code = models.CharField(max_length=16, verbose_name=u'Sigla')
    campus = models.ForeignKey(Campus)

    # Temporal fields.
    semester = models.IntegerField(choices=[(1, 1), (2, 2)], verbose_name=u'Semestre')
    year = models.IntegerField(choices=make_years(), verbose_name=u'Año')

    # state of the course.
    status = models.BooleanField(default=True, verbose_name=u'Estado')

    teachers = models.ManyToManyField('auth.User', through='CourseTeacher',
                                      blank=True,
                                      verbose_name='Profesores')

    software = models.ManyToManyField('misc.Software',
                                      verbose_name='Software')

    # Added for statistics.
    create_date = models.DateTimeField(auto_now_add=True)

    # overrides the global pre-registrations toggle.
    deactivate_preregistrations = models.BooleanField(default=False)

    class Meta:
        ordering = ('-year', '-semester', 'code', 'campus')

    def count_inscriptions(self):
        count = 0

        for agenda in self.agenda_set.all():
            count += agenda.inscriptions.count()

        return count

    def count_assistants(self):
        assistants = set()

        for agenda in self.agenda_set.all():
            for assistant in agenda.assistants.all():
                assistants.add(assistant)

        return len(assistants)

    def __str__(self):
        return u'%s - %s %d-%d' % (
            self.name, self.campus.name, self.year, self.semester)

    def is_active(self):
        """
        :return: True if the course belongs to this semester or one in the future.
        """
        return self.status and \
               (self.year, self.semester) >= get_year_semester()

    def has_submitted_tests(self):
        for test in self.test_set.all():
            if test.get_submitted_tests():
                return True
        return False

    def has_submitted_pretests(self):
        for pretest in self.pretest_set.all():
            if pretest.pretestupload_set.all():
                return True
        return False

    def get_students(self):
        for agenda in self.agenda_set.all():
            for student in agenda.inscriptions.all():
                yield student.student

    def get_coordinator_assistants(self):
        return self.teachers.filter(groups__name="assistants")

    def get_teachers(self):
        return self.teachers.filter(groups__name="teachers").exclude(groups__name="assistants")

    @models.permalink
    def get_absolute_url(self):
        return 'courses:course_detail', [self.pk]

    @models.permalink
    def get_agendas_url(self):
        return 'courses:course_detail', [self.pk, 'agendas']

    @models.permalink
    def get_sessions_url(self):
        return 'courses:course_detail', [self.pk, 'sessions']

    @models.permalink
    def get_pretests_url(self):
        return 'courses:course_detail', [self.pk, 'pretests']

    @models.permalink
    def get_tests_url(self):
        return 'courses:course_detail', [self.pk, 'tests']

    @models.permalink
    def get_news_url(self):
        return 'courses:course_detail', [self.pk, 'news']

    @models.permalink
    def get_files_url(self):
        return 'courses:course_detail', [self.pk, 'files']

    @models.permalink
    def get_grades_url(self):
        return 'courses:course_grades', [self.pk]

    @models.permalink
    def get_preregistrations_create_url(self):
        return 'preregistrations:preregistration_create', [self.pk]


class Agenda(models.Model):
    day = models.IntegerField(choices=make_days(), verbose_name=u'Día')

    room = models.ForeignKey(Room, verbose_name=u'Sala')

    course = models.ForeignKey(Course, verbose_name=u'Curso')

    block = models.IntegerField(choices=make_blocks(), verbose_name=u'Bloque')

    software = models.ForeignKey(
        'misc.Software',
        verbose_name='Software',
        null=True,
        blank=True)

    inscriptions = models.ManyToManyField(
        'auth.User',
        verbose_name=u'Inscritos',
        blank=True,
        related_name='inscriptions')

    assistants = models.ManyToManyField(
        'auth.User',
        verbose_name=u'Ayudantes',
        blank=True,
        related_name='assistants')

    code = models.CharField(max_length=64, verbose_name="Código de inscripción", null=True, blank=True)

    class Meta:
        ordering = ('day', 'block')

    @models.permalink
    def get_attendance_url(self):
        return 'attendance:show', [self.course.pk, self.pk]

    @models.permalink
    def get_update_url(self):
        return 'attendance:agenda_update', [self.course.pk, self.pk]

    def __str__(self):
        return u'%s %s - %s %s' % (self.get_day_display(), self.get_block_display(),
                                   self.room.name, self.room.campus.name)

    def has_active_tests(self):
        for agenda_test in self.agendatest_set.all():
            if agenda_test.active:
                return True
        return False

    def set_code(self):
        code = str(self.pk) + 'S' + str(self.course.pk) + 'D'
        code += ''.join(random.choice('0123456789ABCDEF') for _ in range(3))
        self.code = code
        return code

    def has_submitted_pretests(self):
        for pretest in self.course.pretest_set.all():
            for pretestupload in pretest.pretestupload_set.all():
                if pretestupload.student.user in self.inscriptions.all():
                    return True
        return False

    def get_submitted_pretests(self, pretest_pk = None):
        if pretest_pk:
            pretests = self.course.pretest_set.filter(pk=pretest_pk)
        else:
            pretests = self.course.pretest_set.all()
        students = self.inscriptions.all()
        pretests_list = []

        for pretest in pretests:
            # [Pretest, pretests_upload, len pretest_upload, reviewed, pending reviews]
            sub_list = [pretest, [], 0, 0, 0]
            for upload in pretest.pretestupload_set.all():
                if upload.student.user in students:
                    sub_list[1].append(upload)
                    if upload.qualification is not None:
                        sub_list[3] += 1
            sub_list[2] = len(sub_list[1])
            sub_list[4] = len(sub_list[1]) - sub_list[3]
            pretests_list.append(sub_list)
        print(pretests_list)
        if len(pretests_list):
            return pretests_list
        else:
            return None


class CourseTeacher(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Profesor')
    course = models.ForeignKey('Course', verbose_name='Curso')
    coordinates = models.BooleanField(verbose_name=u'Coordinador')

    def __str__(self):
        return self.user.username


class CourseGradesConfig(models.Model):
    course = models.OneToOneField('Course', related_name='grades_config', blank=True, null=True)

    grade_tests = models.FloatField(verbose_name=u'% Nota controles')

    grade_pretests = models.FloatField(verbose_name=u'% Nota preinformes')

    grade_assistance = models.FloatField(verbose_name=u'% Nota asistencia')

    show_final_grade = models.BooleanField(default=True, verbose_name=u'Mostrar nota final')

    def __str__(self):
        return self.course.name
