from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.views import generic

from adn3 import mixins
from adn3.services import is_student_of
from .models import Poll
from .forms import PollForm


class PollCreateView(UserPassesTestMixin, mixins.CourseMixin, generic.CreateView):
    model = Poll
    form_class = PollForm

    def form_valid(self, form):
        form.instance.student = self.request.user.student
        form.instance.course = self.get_course()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        previous = Poll.objects.filter(student=self.request.user.student, course=self.get_course())
        if previous.exists():
            return redirect(previous.first().get_absolute_url())

        return super().get(request, *args, **kwargs)

    def test_func(self):
        return is_student_of(self.request.user, self.get_course())


class PollDetailView(UserPassesTestMixin, mixins.CourseMixin, generic.DetailView):
    model = Poll

    def test_func(self):
        return is_student_of(self.request.user, self.get_course())
