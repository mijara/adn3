from django.views import generic
from courses.models import Agenda, Course


class AgendaListView(generic.ListView):
    model = Agenda
    template_name = 'public/agenda_list.html'

    def get_queryset(self):
        return self.request.user.inscriptions.all()


class CourseDetail(generic.DetailView):
    model = Course
    template_name = 'public/course_detail.html'
