from django.views import generic

from adn3.constants import YEAR, SEMESTER
from courses.models import Course


class CourseListView(generic.ListView):
    model = Course
    template_name = 'public/course_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(status=True, year=YEAR, semester=SEMESTER)
        return qs


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'public/course_detail.html'
