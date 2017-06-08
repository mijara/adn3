from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from adn3 import mixins
from .forms import *


class CourseFileDetailView(mixins.CourseMixin, generic.DetailView):
    model = CourseFile


class CourseFileCreateView(mixins.CourseMixin, generic.CreateView):
    model = CourseFile
    form_class = CourseFileForm

    def form_valid(self, form):
        form.instance.course = self.get_course()
        return super(CourseFileCreateView, self).form_valid(form)


class CourseFileUpdateView(mixins.CourseMixin, generic.UpdateView):
    model = CourseFile
    form_class = CourseFileForm


class CourseFileDeleteView(mixins.CourseMixin, generic.DeleteView):
    model = CourseFile

    def get_success_url(self):
        return self.get_course().get_files_url()


def download(request, course_pk, pk):
    course_file = get_object_or_404(CourseFile, pk=pk)

    course_file.downloads += 1
    course_file.save()

    # FIXME: is this a security hazard?
    return redirect(course_file.file.url)
