from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from adn3.services import get_period_year, get_period_semester
from adn3.mixins import CourseMixin
from coordination.services import generate_excel, generate_polls_excel
from adn3.services import preregistrations_open, preregistrations_set, \
    is_coordinator, registrations_open, registrations_set, polls_open, polls_set
from courses.models import Course
from misc.models import Software
from polls.models import Poll


class CoordinatorTestMixin(UserPassesTestMixin):
    def test_func(self):
        return is_coordinator(self.request.user)


class CoordinationIndexView(CoordinatorTestMixin, View):
    def get(self, request):
        current_courses = Course.objects.filter(year=get_period_year(), semester=get_period_semester())

        return render(request, 'coordination/coordination_index.html', {
            'current_courses': current_courses,
            'software_list': Software.objects.all(),
            'preregistrations_open': preregistrations_open(),
            'registrations_open': registrations_open(),
            'polls_open': polls_open(),
        })


class PreRegistrationExcelView(CoordinatorTestMixin, View):
    def get(self, request):
        course = self.get_course()
        software = self.get_software()

        pr_list = course.flyin_set.filter(software=software).order_by('pk')
        content = generate_excel(course, software, pr_list)

        response = HttpResponse(
            content=content,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=preinscripciones.xlsx'
        return response

    def get_course(self):
        course_pk = self.request.GET.get('course')

        if course_pk is None:
            raise Http404()

        return get_object_or_404(Course, pk=course_pk)

    def get_software(self):
        software_pk = self.request.GET.get('software')

        if software_pk is None:
            raise Http404()

        return get_object_or_404(Software, pk=software_pk)


class PreRegistrationsScheduleView(CoordinatorTestMixin, CourseMixin, View):
    def get(self, request, course_pk, software_pk):
        flyins = self.get_course().flyin_set.filter(software_id=software_pk)

        return render(request, 'coordination/course_schedule.html', {
            'view': self,
            'software': get_object_or_404(Software, pk=software_pk),
            'pr_count': flyins.count()
        })


class PreRegistrationsToggle(CoordinatorTestMixin, View):
    def get(self, request):
        state = preregistrations_open()
        preregistrations_set(not state)

        return redirect('coordination:coordination_index')


class RegistrationsToggle(CoordinatorTestMixin, View):
    def get(self, request):
        state = registrations_open()
        registrations_set(not state)

        return redirect('coordination:coordination_index')


class PollsToggle(CoordinatorTestMixin, View):
    def get(self, request):
        state = polls_open()
        polls_set(not state)

        return redirect('coordination:coordination_index')


class PollsExcelView(CoordinatorTestMixin, View):
    def get(self, request):
        course = self.get_course()

        poll_list = Poll.objects.filter(course=course).order_by('pk')
        print(poll_list)
        content = generate_polls_excel(course, poll_list)

        response = HttpResponse(
            content=content,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=encuesta-{filename}.xlsx'.format(filename=str(course))
        return response

    def get_course(self):
        course_pk = self.request.GET.get('course')

        if course_pk is None:
            raise Http404()

        return get_object_or_404(Course, pk=course_pk)