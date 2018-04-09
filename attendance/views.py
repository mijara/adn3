from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from attendance.forms import AgendaForm, AgendaAddAssistantForm, AgendaDeleteAssistantsForm, AgendaAddInscriptionForm, \
    AgendaDeleteInscriptionsForm
from courses.models import Agenda
from .services import *
from adn3.services import is_teacher_of, is_coordinator
from adn3.mixins import CourseMixin
from django.views import View
from django.views.generic import UpdateView, FormView


class HasAccessToAttendanceMixin(UserPassesTestMixin):
    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course()) or is_coordinator(self.request.user)


class SaveAttendanceView(HasAccessToAttendanceMixin, CourseMixin, View):
    def post(self, request, course_pk, agenda_pk):
        agenda = get_object_or_404(Agenda, pk=agenda_pk)
        save_matrix(agenda, request.POST)
        return redirect('attendance:show', course_pk, agenda_pk)


class AttendanceDetailView(HasAccessToAttendanceMixin, CourseMixin, View):
    def get(self, request, course_pk, agenda_pk):
        agenda = get_object_or_404(Agenda, pk=agenda_pk)

        try:
            table = create_matrix(agenda)
        except:
            table = None

        return render(request, 'attendance/agenda_detail.html', {
            'view': self,
            'agenda': agenda,
            'table': table,
            'ACTIVE': 'agendas',
            'section': 'agendas',
            'course': self.get_course()
        })


class AgendaUpdateView(HasAccessToAttendanceMixin, CourseMixin, UpdateView):
    pk_url_kwarg = 'agenda_pk'
    model = Agenda
    form_class = AgendaForm
    template_name = 'attendance/agenda_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_assistant_form'] = AgendaAddAssistantForm()
        context['add_inscription_form'] = AgendaAddInscriptionForm()
        return context


class AgendaDeleteAssistantsView(HasAccessToAttendanceMixin, CourseMixin, FormView):
    form_class = AgendaDeleteAssistantsForm
    template_name = 'form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['agenda_pk'] = self.kwargs['agenda_pk']
        return kwargs

    def get_success_url(self):
        return reverse('attendance:agenda_update', args=[self.kwargs['course_pk'], self.kwargs['agenda_pk']])

    def form_valid(self, form):
        response = super().form_valid(form)

        agenda = get_object_or_404(Agenda, pk=self.kwargs['agenda_pk'])

        for assistant_pk in form.cleaned_data['assistants']:
            agenda.assistants.remove(assistant_pk)

        return response

    def form_invalid(self, form):
        return redirect(self.get_success_url())


class AgendaAddAssistantView(HasAccessToAttendanceMixin, CourseMixin, FormView):
    form_class = AgendaAddAssistantForm
    template_name = 'form.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        assistant = get_object_or_404(User, email=form.cleaned_data['assistant'])
        agenda = get_object_or_404(Agenda, pk=self.kwargs['agenda_pk'])
        agenda.assistants.add(assistant)

        return response

    def get_success_url(self):
        return reverse('attendance:agenda_update', args=[self.kwargs['course_pk'], self.kwargs['agenda_pk']])


class AgendaDeleteInscriptionsView(HasAccessToAttendanceMixin, CourseMixin, FormView):
    form_class = AgendaDeleteInscriptionsForm
    template_name = 'form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['agenda_pk'] = self.kwargs['agenda_pk']
        return kwargs

    def get_success_url(self):
        return reverse('attendance:agenda_update', args=[self.kwargs['course_pk'], self.kwargs['agenda_pk']])

    def form_valid(self, form):
        response = super().form_valid(form)

        agenda = get_object_or_404(Agenda, pk=self.kwargs['agenda_pk'])

        for inscription_pk in form.cleaned_data['inscriptions']:
            agenda.inscriptions.remove(inscription_pk)

        return response

    def form_invalid(self, form):
        return redirect(self.get_success_url())


class AgendaAddInscriptionView(HasAccessToAttendanceMixin, CourseMixin, FormView):
    form_class = AgendaAddInscriptionForm
    template_name = 'form.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        inscription = get_object_or_404(User, email=form.cleaned_data['inscription'])
        agenda = get_object_or_404(Agenda, pk=self.kwargs['agenda_pk'])
        agenda.inscriptions.add(inscription)

        return response

    def get_success_url(self):
        return reverse('attendance:agenda_update', args=[self.kwargs['course_pk'], self.kwargs['agenda_pk']])
