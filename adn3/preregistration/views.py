from django.views import generic
from django.views import View
from courses.models import Course


class CoursePreRegistrationDetailView(generic.DetailView):
    model = Course
    template_name = 'preregistration/course_detail.html'
