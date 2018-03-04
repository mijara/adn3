from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from adn3.services import is_teacher, is_student, is_coordinator

from adn3.constants import YEAR, SEMESTER
from courses.models import *
from django.views import generic


@method_decorator(login_required, 'dispatch')
class CourseListView(UserPassesTestMixin, generic.ListView):
    model = Course
    template_name = 'teachers/course_list.html'

    def get_queryset(self):
        if is_coordinator(self.request.user):
            return Course.objects.filter(year=YEAR, semester=SEMESTER)

        campuses = [st.campus for st in self.request.user.superteacher_set.all() if st.campus]

        course_set = self.request.user.course_set.filter(year=YEAR, semester=SEMESTER)

        if len(campuses) != 0:
            campus_courses_set = Course.objects.filter(year=YEAR, semester=SEMESTER, campus__in=campuses)
            return campus_courses_set | course_set

        return course_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['old_course_list'] = self.request.user.course_set.exclude(year=YEAR, semester=SEMESTER)
        return context

    def test_func(self):
        return is_teacher(self.request.user) and not is_student(self.request.user)
