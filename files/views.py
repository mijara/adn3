import base64

import io
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View

from adn3 import mixins
from files.services import register_file_download
from .forms import *
import matplotlib.pyplot as plt


class CourseFileDetailView(mixins.CourseMixin, generic.DetailView):
    model = CourseFile

    def graph_downloads(self):
        data = self.object.coursefiledownload_set.all()

        dates = [d.timestamp.strftime('%d/%m') for d in data]
        plt.gcf().set_size_inches((8, 2.5))
        plt.hist(dates, color='k')
        plt.gcf().autofmt_xdate()
        plt.gcf().tight_layout()

        sio = io.BytesIO()
        plt.savefig(sio, format="png")

        return base64.b64encode(sio.getvalue())


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


class CourseFileDownloadView(View):
    def get(self, *args, **kwargs):
        pk = self.kwargs.pop('pk')
        course_file = get_object_or_404(CourseFile, pk=pk)

        course_file.downloads += 1
        course_file.save()

        register_file_download(course_file, self.request.user)

        # FIXME: is this a security hazard?
        return redirect(course_file.file.url)
