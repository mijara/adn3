from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from adn3.services import is_teacher, is_student, is_coordinator

from adn3.services import get_period_year, get_period_semester
from courses.models import *
from django.views import generic, View


@method_decorator(login_required, 'dispatch')
class CourseListView(UserPassesTestMixin, generic.ListView):
    model = Course
    template_name = 'teachers/course_list.html'

    def get_queryset(self):
        if is_coordinator(self.request.user):
            return Course.objects.filter(year=get_period_year(), semester=get_period_semester())

        campuses = [st.campus for st in self.request.user.superteacher_set.all() if st.campus]

        course_set = self.request.user.course_set.filter(year=get_period_year(), semester=get_period_semester())

        if len(campuses) != 0:
            campus_courses_set = Course.objects.filter(year=get_period_year(),
                                                       semester=get_period_semester(),
                                                       campus__in=campuses)
            return campus_courses_set | course_set

        return course_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if is_coordinator(self.request.user):
            course_set = Course.objects
        else:
            course_set = self.request.user.course_set

        context['old_course_list'] = course_set.exclude(
            year=get_period_year(),
            semester=get_period_semester())

        return context

    def test_func(self):
        return is_teacher(self.request.user)


class TeacherPasswordUpdateView(View):
    def get(self, request):
        form = PasswordChangeForm(self.request.user)

        return render(request, 'teachers/teacher_password_update.html', context={
            'form': form,
        })

    def post(self, request):
        form = PasswordChangeForm(self.request.user, data=self.request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('teachers:index')

        return render(request, 'teachers/teacher_password_update.html', context={
            'form': form,
        })
