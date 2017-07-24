from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^create/$',
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
        '^reserve-attempt/create/$',
        views.ReserveAttemptCreateView.as_view(),
        name='reserveattempt_create'
    ),

    url(
        '^reserve-attempt/detail/(?P<pk>.*)/$',
        views.ReserveAttemptDetailView.as_view(),
        name='reserveattempt_detail'
    ),
]
