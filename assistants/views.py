from adn3 import mixins
from django.views import generic, View
from django.shortcuts import render
from courses.models import Agenda
from django.shortcuts import get_object_or_404, redirect
from tests.models import Test
from pretests.models import PretestUpload
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from attendance.services import *

from adn3.services import is_assistant_of, is_assistant_of_agenda

from django.contrib.auth.mixins import UserPassesTestMixin


class CourseListView(generic.View):
    def get(self, request):
        agendas = self.request.user.assistants.all()
        courses = []
        for a in agendas:
            if a.course not in courses:
                courses.append(a.course)
        return render(self.request, 'assistants/course_list.html', {'courses': courses})


class CourseDetailView(UserPassesTestMixin, mixins.CourseMixin, generic.View):
    def get(self, request, course_pk, section='attendance'):
        return render(self.request, 'assistants/course_detail.html', {
            'view': self,
            'course': self.get_course(),
            'ACTIVE': section,
            'section': section,
            'agendas': self.request.user.assistants.filter(course=self.get_course()),
            'tests': Test.objects.filter(course=self.get_course())
        })

    def test_func(self):
        return is_assistant_of(self.request.user, self.get_course())


class AttendanceView(UserPassesTestMixin, mixins.CourseMixin, View):
    def get(self, request, course_pk, agenda_pk):
        agenda = get_object_or_404(Agenda, pk=agenda_pk)

        try:
            table = create_matrix(agenda)
        except:
            table = None

        return render(request, 'assistants/attendance.html', {
            'view': self,
            'agenda': agenda,
            'ACTIVE': 'agendas',
            'table': table,
            'section': 'agendas',
            'course': self.get_course()
        })

    def test_func(self):
        agenda = get_object_or_404(Agenda, pk=self.kwargs['agenda_pk'])
        return is_assistant_of_agenda(self.request.user, agenda)


class AttendanceSaveView(UserPassesTestMixin, mixins.CourseMixin, View):
    def post(self, request, course_pk, agenda_pk):
        agenda = get_object_or_404(Agenda, pk=agenda_pk)
        save_matrix(agenda, request.POST)
        return redirect('assistants:course_detail', course_pk)

    def test_func(self):
        agenda = get_object_or_404(Agenda, pk=self.kwargs['agenda_pk'])
        return is_assistant_of_agenda(self.request.user, agenda)


class InscriptionEnableView(UserPassesTestMixin, mixins.CourseMixin, View):
    def get(self, request, course_pk, agenda_pk):
        agenda = get_object_or_404(Agenda, pk=agenda_pk)
        agenda.set_code()
        agenda.save()
        return redirect('assistants:course_detail', course_pk)

    def test_func(self):
        agenda = get_object_or_404(Agenda, pk=self.kwargs['agenda_pk'])
        return is_assistant_of_agenda(self.request.user, agenda)


class PretestReviewListView(UserPassesTestMixin, mixins.CourseMixin, generic.DetailView):
    model = Agenda
    template_name = 'assistants/pretest_students_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pretest'] = self.get_object().get_submitted_pretests(self.kwargs['pretest_pk'])[0]
        return context

    def test_func(self):
        agenda = self.get_object()
        return is_assistant_of_agenda(self.request.user, agenda)


class PretestReviewView(UserPassesTestMixin, generic.DetailView):
    model = PretestUpload
    template_name = "assistants/pretest_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agenda'] = get_object_or_404(Agenda, pk=self.kwargs['agenda_pk'])
        return context


    def post(self, request, *args, **kwargs):
        pretest = self.get_object()
        pretest.qualification = request.POST.get('grade')
        pretest.feedback = request.POST.get('feedback')
        pretest.save()

        pretests_list_url = reverse('assistants:pretest_review_list', args=[kwargs['course_pk'], kwargs['agenda_pk'], kwargs['pretest_pk']])
        if request.POST.get('action') == "close-after":
            return HttpResponseRedirect(pretests_list_url + '?message=success')
        elif request.POST.get('action') == "next-after":
            next_ = PretestUpload.objects.filter(pretest__pk=kwargs['pretest_pk'], qualification=None).first()
            if next_:
                return HttpResponseRedirect(next_.get_review_url())
            else:
                return HttpResponseRedirect(pretests_list_url + '?message=nomore')

    def test_func(self):
        agenda = get_object_or_404(Agenda, pk=self.kwargs['agenda_pk'])
        return is_assistant_of_agenda(self.request.user, agenda)
