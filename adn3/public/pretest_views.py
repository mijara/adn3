from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from pretests.forms import PretestUploadForm
from pretests.models import Pretest, PretestUpload


class PretestMixin:
    def get_pretest(self):
        return get_object_or_404(Pretest, pk=self.kwargs['pretest_pk'])


class PretestDetailView(generic.DetailView):
    model = Pretest
    template_name = 'public/pretest_detail.html'

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

    template_name = 'public/pretest_detail.html'

    def form_valid(self, form):
        form.instance.pretest = self.get_pretest()
        form.instance.student = self.request.user.student
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('public:pretest_detail', args=[self.object.pretest.pk])
