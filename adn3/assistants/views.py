from adn3 import mixins
from django.views import generic
from django.shortcuts import render
from courses.models import Agenda
from tests.models import Test


class CourseListView(generic.View):
    def get(self, request):
        agendas = self.request.user.assistants.all()
        courses = []
        for a in agendas:
            if a.course not in courses:
                courses.append(a.course)
        return render(self.request, 'assistants/course_list.html', {'courses': courses})

class CourseDetailView(mixins.CourseMixin, generic.View):
    def get(self, request, course_pk, section='attendance'):
        return render(self.request, 'assistants/course_detail.html', {
            'view': self,
            'course': self.get_course(),
            'ACTIVE': section,
            'section': section,
            'agendas': self.request.user.assistants.filter(course=self.get_course()),
            'tests': Test.objects.filter(course=self.get_course())
        })