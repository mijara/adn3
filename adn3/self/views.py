from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from courses.models import *
from django.views import generic


@method_decorator(login_required, 'dispatch')
class CourseListView(generic.ListView):
    model = Course
    template_name = 'self/teachers/course_list.html'
