from django.core.urlresolvers import reverse_lazy
from django.views import generic

from adn3 import mixins
from forms import *


class NewDetail(generic.DetailView):
    model = New


class NewUpdate(mixins.CourseMixin, generic.UpdateView):
    model = New
    form_class = NewForm


class NewCreate(mixins.CourseMixin, generic.CreateView):
    model = New
    form_class = NewForm

    def form_valid(self, form):
        form.instance.course = self.get_course()
        form.instance.owner = self.request.user
        return super(NewCreate, self).form_valid(form)


class NewDelete(mixins.GoBackPageMixin, mixins.CourseMixin,
                generic.DeleteView):
    model = New

    def get_success_url(self):
        return self.get_course().get_news_url()
