from django.views import generic

from adn3 import mixins
from forms import *


class TestList(mixins.CourseMixin, generic.ListView):
    def get_queryset(self):
        return self.get_course().test_set.all()


class TestDetail(generic.DetailView):
    model = Test


class TestCreate(mixins.CourseMixin, generic.CreateView):
    model = Test
    form_class = TestForm

    def get_form(self, form_class=None):
        form = super(TestCreate, self).get_form(form_class)
        form.fields['session'].queryset = self.get_course().session_set
        return form

    def form_valid(self, form):
        form.instance.course = self.get_course()
        form.instance.owner = self.request.user
        return super(TestCreate, self).form_valid(form)


class TestUpdate(mixins.CourseMixin, generic.UpdateView):
    model = Test
    form_class = TestForm
