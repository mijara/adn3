from django.views import generic
from pretests.models import Pretest, PretestUpload


class PretestDetailView(generic.DetailView):
    model = Pretest
