from django.views import generic

from adn3 import mixins
from courses.views import IsTeacherOfCourseMixin
from .forms import *


class NewDetail(IsTeacherOfCourseMixin, mixins.CourseMixin, generic.DetailView):
    model = New


class NewUpdate(IsTeacherOfCourseMixin, mixins.CourseMixin, generic.UpdateView):
    model = New
    form_class = NewForm


class NewCreate(IsTeacherOfCourseMixin, mixins.CourseMixin, generic.CreateView):
    model = New
    form_class = NewForm

    def form_valid(self, form):
        form.instance.course = self.get_course()
        form.instance.owner = self.request.user
        return super(NewCreate, self).form_valid(form)


class NewDelete(mixins.GoBackPageMixin, IsTeacherOfCourseMixin, mixins.CourseMixin,
                generic.DeleteView):
    model = New

    def get_success_url(self):
        return self.get_course().get_news_url()
