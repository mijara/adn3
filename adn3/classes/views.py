from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from adn3 import mixins
from .forms import *
from datetime import timedelta
from .services import *


class SessionMixin(mixins.CourseMixin):
    def get_session(self):
        print(1)
        return get_object_or_404(Session, pk=self.kwargs['session_pk'])


class SessionDetailView(generic.DetailView):
    model = Session


class SessionCreateView(mixins.CourseMixin, generic.CreateView):
    model = Session
    form_class = SessionForm

    def get_initial(self):
        return {
            'number': get_first_available(self.get_course().session_set.all()),
            'start_date': datetime.now(),
            'end_date': datetime.now() + timedelta(days=5)
        }

    def form_valid(self, form):
        form.instance.course = self.get_course()
        return super(SessionCreateView, self).form_valid(form)


class SessionUpdateView(mixins.CourseMixin, generic.UpdateView):
    model = Session
    form_class = SessionForm


class SessionDeleteView(mixins.CourseMixin, generic.DeleteView):
    model = Session

    def get_success_url(self):
        return self.get_course().get_sessions_url()


class SessionFileCreateView(SessionMixin, generic.CreateView):
    model = SessionFile
    form_class = SessionFileForm

    def form_valid(self, form):
        form.instance.session = self.get_session()
        return super().form_valid(form)

    def get_success_url(self):
        return self.get_session().get_absolute_url()


class SessionFileDeleteView(SessionMixin, generic.DeleteView):
    model = SessionFile

    def get_success_url(self):
        return self.get_session().get_absolute_url()
