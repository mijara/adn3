from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^course/(?P<course_pk>\d+)/$',
        views.CourseDetailView.as_view(),
        name='course_detail'
    ),

    url(
        '^course/(?P<course_pk>\d+)/attendance/(?P<agenda_pk>\d+)/$',
        views.AttendanceView.as_view(),
        name='attendance'
    ),

    url(
        '^course/(?P<course_pk>\d+)/attendance/(?P<agenda_pk>\d+)/save/$',
        views.AttendanceSaveView.as_view(),
        name='attendance_save'
    ),

    url(
        '^course/(?P<course_pk>\d+)/inscription/(?P<agenda_pk>\d+)/enable',
        views.InscriptionEnableView.as_view(),
        name='enable_inscription'
    ),
]
