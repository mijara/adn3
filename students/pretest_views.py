from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.forms.utils import ErrorList


from pretests.forms import PretestUploadForm
from pretests.models import Pretest, PretestUpload


class PretestMixin:
    def get_pretest(self):
        return get_object_or_404(Pretest, pk=self.kwargs['pretest_pk'])


class PretestDetailView(generic.DetailView):
    model = Pretest
    template_name = 'students/pretest_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # check if the user has already uploaded an answer.
        try:
            context['pretestupload'] = self.request.user.student.pretestupload_set.get(pretest_id=self.object.pk)
        except PretestUpload.DoesNotExist:
            context['pretestupload'] = None

        context['form'] = PretestUploadForm()

        return context


class PretestUploadCreateView(PretestMixin, generic.CreateView):
    model = PretestUpload
    form_class = PretestUploadForm

    template_name = 'students/pretest_detail.html'

    def form_valid(self, form):
        pretest = self.get_pretest()
        if not pretest.online:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList([
                u'Este preinforme es de entrega presencial'
            ])
            return self.form_invalid(form)
        form.instance.pretest = pretest
        form.instance.student = self.request.user.student
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('students:pretest_detail', args=[self.object.pretest.pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # check if the user has already uploaded an answer.
        context['pretest'] = self.get_pretest()
        try:
            context['pretestupload'] = self.request.user.student.pretestupload_set.get(pretest_id=self.get_pretest())
        except PretestUpload.DoesNotExist:
            context['pretestupload'] = None

        context['form'] = PretestUploadForm()

        return context
