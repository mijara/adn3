from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from adn3 import mixins
from .forms import *
from datetime import timedelta
from .services import *


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


def upload(request, pk):
    session = get_object_or_404(Session, pk=pk)

    form = SessionFileForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.session = session
            instance.save()

            return redirect('classes:session_detail', session.pk)

    return render(request, 'classes/upload.html', {
        'session': session,
        'form': form
    })


def remove_file(request, file_pk):
    session_file = get_object_or_404(SessionFile, pk=file_pk)

    session_pk = session_file.session.pk

    session_file.file.delete()
    session_file.delete()

    return redirect('classes:session_detail', session_pk)
