from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import generic
from courses.models import Course
from preregistration.models import PreRegistration
from .forms import PreRegistrationForm
from adn3 import mixins


class PreRegistrationDetailView(generic.DetailView):
    model = PreRegistration


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


class CourseDetailView(generic.DetailView, LoginRequiredMixin):
    model = Course
    template_name = 'preregistration/course_detail.html'


class CourseListView(generic.ListView):
    model = Course
    template_name = 'preregistration/course_list.html'
