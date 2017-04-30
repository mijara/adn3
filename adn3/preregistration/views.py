from django.views import generic
from courses.models import Course
from preregistration.models import PreRegistration
from .forms import PreRegistrationForm
from adn3 import mixins


class CoursePreRegistrationDetailView(generic.DetailView):
    model = Course
    template_name = 'preregistration/course_detail.html'


class PreRegistrationCreateView(mixins.CourseMixin, generic.CreateView):
    model = PreRegistration
    form_class = PreRegistrationForm

    def form_valid(self, form):
        form.instance.course = self.get_course()
        return super(PreRegistrationCreateView, self).form_valid(form)

    def get_initial(self):
        initial = super(PreRegistrationCreateView, self).get_initial()
        initial['course'] = self.get_course()
        return initial
