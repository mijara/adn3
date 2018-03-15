from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.CoordinationIndexView.as_view(),
        name='coordination_index'
    ),

    url(
        r'^preregistrations/excel/$',
        views.PreRegistrationExcelView.as_view(),
        name='preregistrations_excel'
    ),

    url(
        r'^preregistrations/overview/excel/$',
        views.PreRegistrationOverviewExcelView.as_view(),
        name='preregistrations_overview_excel'
    ),

    url(
        r'^preregistrations/schedule/(?P<course_pk>\d+)/(?P<software_pk>\d+)/$',
        views.PreRegistrationsScheduleView.as_view(),
        name='preregistrations_schedule'
    ),

    url(
        r'^preregistrations/toggle/$',
        views.PreRegistrationsToggle.as_view(),
        name='preregistrations_toggle'
    ),

    url(
        r'^registrations/toggle/$',
        views.RegistrationsToggle.as_view(),
        name='registrations_toggle'
    ),

    url(
        r'^polls/toggle/$',
        views.PollsToggle.as_view(),
        name='polls_toggle'
    ),

    url(
        r'^polls/excel/$',
        views.PollsExcelView.as_view(),
        name='polls_excel'
    ),
]
