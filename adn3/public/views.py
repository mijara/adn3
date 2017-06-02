from django.views import generic

from adn3.services import is_assistant_of
from courses.models import Agenda, Course


class AgendaListView(generic.ListView):
    model = Agenda
    template_name = 'public/agenda_list.html'

    def get_queryset(self):
        return self.request.user.inscriptions.all() | self.request.user.assistants.all()


class CourseDetail(generic.DetailView):
    model = Course
    template_name = 'public/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # check if the user is assistant of the course.
        context['assistant'] = None
        for agenda in self.object.agenda_set.all():
            if is_assistant_of(self.request.user, agenda):
                context['assistant'] = agenda
        return context
