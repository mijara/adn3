from django.views import generic
from courses.models import Course


class CourseList(generic.ListView):
    model = Course
    template_name = 'public/course_list.html'


class CourseDetail(generic.DetailView):
    model = Course
    template_name = 'public/course_detail.html'
