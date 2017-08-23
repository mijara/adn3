from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^show/(?P<agenda_pk>\d+)/$',
        views.ShowAttendanceView.as_view(),
        name='show'
    ),

    url(
        '^save/(?P<agenda_pk>\d+)/$',
        views.SaveAttendanceView.as_view(),
        name='save'
    ),
]
