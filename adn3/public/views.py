from django.views import generic
from courses.models import Course
from tests.models import Version


class CourseList(generic.ListView):
    model = Course
    template_name = 'public/course_list.html'


class CourseDetail(generic.DetailView):
    model = Course
    template_name = 'public/course_detail.html'

class Test(generic.DetailView):
    model = Version
    template_name = 'public/test.html'
