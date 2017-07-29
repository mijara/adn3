from django.views import generic


class CoordinationIndexView(generic.TemplateView):
    template_name = 'coordination/coordination_index.html'
