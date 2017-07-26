from django.shortcuts import get_object_or_404
from courses.models import Course, Agenda
from tests.models import Test, Version


class CourseMixin(object):
    def get_course(self):
        return get_object_or_404(Course, pk=self.kwargs['course_pk'])


class GoBackPageMixin(object):
    def get_last_page(self):
        return self.request.META['HTTP_REFERER']
