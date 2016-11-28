from django.shortcuts import get_object_or_404
from courses.models import Course
from tests.models import Test, Version


class CourseMixin(object):
    def get_course(self):
        return get_object_or_404(Course, pk=self.kwargs['course_pk'])


class TestMixin(object):
    def get_test(self):
        return get_object_or_404(Test, pk=self.kwargs['test_pk'])

    def get_course(self):
        return get_object_or_404(Test, pk=self.kwargs['test_pk']).course


class VersionMixin(object):
    def get_version(self):
        return get_object_or_404(Version, pk=self.kwargs['version_pk'])

    def get_test(self):
        return get_object_or_404(Version, pk=self.kwargs['version_pk']).test

    def get_course(self):
        return get_object_or_404(Version, pk=self.kwargs['version_pk']).test.course


class GoBackPageMixin(object):
    def get_last_page(self):
        return self.request.META['HTTP_REFERER']
