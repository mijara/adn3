from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^$',
        views.StudentCreateView.as_view(),
        name='student_create'
    ),

    url(
        '^update/$',
        views.StudentUpdateView.as_view(),
        name='student_detail'
    ),

    url(
        '^update-password/$',
        views.StudentPasswordUpdateView.as_view(),
        name='student_password_update'
    ),

    url(
        '^success/$',
        views.StudentSuccessView.as_view(),
        name='student_success'
    ),

    url(
        '^ticket/create/$',
        views.TicketCreateView.as_view(),
        name='ticket_create'
    ),

    url(
        '^ticket/(?P<pk>.*)/$',
        views.TicketDetailView.as_view(),
        name='ticket_detail'
    ),
]
