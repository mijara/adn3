from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views import View

from adn3.services import preregistrations_open
from courses.models import Course
from misc.models import Software
from news.models import New
from .models import FlyIn
from .forms import FlyInForm, RolForm, DeleteForm
from adn3 import mixins


class FlyInsActiveMixin(UserPassesTestMixin):
    login_url = reverse_lazy('flyins:rol_authentication')

    def test_func(self):
        is_authenticated = self.request.session.get('rol', False)
        return preregistrations_open() and is_authenticated


class RolAuthenticationView(UserPassesTestMixin, View):
    template_name = 'flyins/rol_authentication.html'

    def get(self, request):
        if request.session.get('rol', False):
            return redirect(reverse_lazy('flyins:course_list'))
        return render(request, self.template_name)

    def post(self, request):
        initial = {
            'rol': self.request.POST.get('rol')
        }
        form = RolForm(initial)

        if form.is_valid():
            request.session.set_expiry(1200)
            request.session['rol'] = self.request.POST.get('rol')

            return redirect(reverse_lazy('flyins:course_list'))
        else:
            return render(request, self.template_name, {
                'form': form
            })

    def test_func(self):
        return preregistrations_open()


class CourseListView(FlyInsActiveMixin, generic.ListView):
    model = Course
    template_name = 'flyins/course_list.html'

    def get_queryset(self):
        # Filter courses already pre-registered and courses on another campus.
        return super().get_queryset().exclude(status=False)


class NewListView(FlyInsActiveMixin, mixins.CourseMixin, generic.ListView):
    model = New
    template_name = 'flyins/new_list.html'

    def get_queryset(self):
        return self.get_course().new_set


class FlyInDetailView(FlyInsActiveMixin, generic.DetailView):
    model = FlyIn

    def get(self, request, *args, **kwargs):
        preinscription = self.get_object()
        if preinscription.rol != self.request.session.get('rol') or preinscription.seen:
            return redirect(reverse_lazy('flyins:course_list'))

        preinscription.seen = True
        preinscription.save()

        return super().get(self, request, *args, **kwargs)


class FlyInCreateView(FlyInsActiveMixin, mixins.CourseMixin, View):
    template_name = 'flyins/preregistration_form.html'
    form_class = FlyInForm

    def get(self, request, course_pk):
        rol = self.request.session.get('rol', False)
        course = self.get_course()

        preinscription = FlyIn.objects.filter(rol=rol, course__pk=course_pk).first()
        print(preinscription)
        if preinscription:
            return redirect(preinscription.get_delete_url())

        # has_pr = FlyIn.objects.filter(rol=rol, course=course).exists()
        # if has_pr:
        # return render(request, 'flyins/preregistration_exists.html', {
        #         'course': course,
        #     })

        return render(request, self.template_name, {
            'software_list': Software.objects.all(),
            'course': course,
            'view': self,
        })

    def post(self, request, course_pk):
        rol = self.request.session.get('rol', False)

        preinscription = FlyIn.objects.filter(rol=rol, course__pk=course_pk).first()

        if preinscription:
            return redirect(preinscription.get_delete_url())

        preferences = request.POST.getlist('block')
        sel_names = ['first_preference', 'second_preference', 'third_preference',
                     'fourth_preference', 'fifth_preference']
        selections = {}

        for i, p in enumerate(sel_names):
            selections[p] = preferences[i] if len(preferences) > i else ''

        initial = {
            'course': self.get_course().pk,
            'software': self.request.POST.get('software'),
            'previous_experience': self.request.POST.get('previous_experience'),
            'parallel': self.request.POST.get('parallel'),
            'first_name': self.request.POST.get('first_name'),
            'last_names': self.request.POST.get('last_names'),
            'rol': self.request.POST.get('rol'),
            'usm_priority': self.request.POST.get('usm_priority').replace(',', '.'),
        }
        initial.update(selections)

        form = FlyInForm(initial)

        if form.is_valid():
            instance = form.save()
            return redirect(instance.get_absolute_url())

        return render(request, self.template_name, {
            'form': form,
            'course': self.get_course(),
            'view': self,
        })


class FlyInDeleteView(FlyInsActiveMixin, View):
    template_name = 'flyins/flyin_confirm_delete.html'

    def get(self, request, pk):
        rol = self.request.session.get('rol', False)

        preinscription = FlyIn.objects.filter(rol=rol, pk=pk).first()

        if not preinscription:
            return redirect(reverse_lazy('flyins:course_list'))

        return render(request, self.template_name, {
            'flyin': preinscription
        })

    def post(self, request, pk):
        rol = self.request.session.get('rol', False)

        preinscription = FlyIn.objects.filter(rol=rol, pk=pk).first()

        if not preinscription:
            return redirect(reverse_lazy('flyins:course_list'))

        secret = self.request.POST.get('secret') if self.request.POST.get('secret') is not None else "NULL"

        initial = {
            'rol': self.request.POST.get('rol'),
            'secret': secret,
            'pk': self.request.POST.get('pk'),
        }

        form = DeleteForm(initial)

        if form.is_valid():
            re = reverse_lazy('flyins:preregistration_create', args=[preinscription.course.pk])
            preinscription.delete()
            return redirect(re)

        return render(request, self.template_name, {
            'form': form,
            'flyin': preinscription,
        })
