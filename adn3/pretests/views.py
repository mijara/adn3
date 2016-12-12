from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from adn3 import mixins
from forms import *


class PretestDetailView(generic.DetailView):
    model = Pretest


class PretestUpdateView(mixins.CourseMixin, generic.UpdateView):
    model = Pretest
    form_class = PretestForm


class PretestCreateView(mixins.CourseMixin, generic.CreateView):
    model = Pretest
    form_class = PretestForm

    def form_valid(self, form):
        form.instance.course = self.get_course()
        return super(PretestCreateView, self).form_valid(form)


class PretestDeleteView(mixins.CourseMixin, generic.DeleteView):
    model = Pretest

    def get_success_url(self):
        return self.get_course().get_pretests_url()


def pretestfile_create(request, pk):
    pretest = get_object_or_404(Pretest, pk=pk)

    form = PretestFileForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.pretest = pretest
            instance.save()

            return redirect(pretest.get_absolute_url())

    return render(request, 'pretests/upload.html', {
        'pretest': pretest,
        'form': form
    })


def pretestfile_delete(request, pk):
    instance = get_object_or_404(PretestFile, pk=pk)

    pretest = instance.pretest

    instance.file.delete()
    instance.delete()

    return redirect(pretest.get_absolute_url())
