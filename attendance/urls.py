from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^show/(?P<agenda_pk>\d+)/$',
        views.AttendanceDetailView.as_view(),
        name='show'
    ),

    url(
        '^save/(?P<agenda_pk>\d+)/$',
        views.SaveAttendanceView.as_view(),
        name='save'
    ),

    url(
        '^(?P<agenda_pk>\d+)/update/$',
        views.AgendaUpdateView.as_view(),
        name='agenda_update'
    ),

    url(
        '^(?P<agenda_pk>\d+)/update/delete-assistants/$',
        views.AgendaDeleteAssistantsView.as_view(),
        name='agenda_update_delete_assistants'
    ),

    url(
        '^(?P<agenda_pk>\d+)/update/add-assistant/$',
        views.AgendaAddAssistantView.as_view(),
        name='agenda_update_add_assistant'
    ),

    url(
        '^(?P<agenda_pk>\d+)/update/delete-inscriptions/$',
        views.AgendaDeleteInscriptionsView.as_view(),
        name='agenda_update_delete_inscriptions'
    ),

    url(
        '^(?P<agenda_pk>\d+)/update/add-inscription/$',
        views.AgendaAddInscriptionView.as_view(),
        name='agenda_update_add_inscription'
    ),
]
