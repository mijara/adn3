from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^(?P<pk>\d+)/$',
        views.PretestDetailView.as_view(),
        name='pretest_detail'
    ),

    url(
        '^(?P<course_pk>\d+)/update/(?P<pk>\d+)/$',
        views.PretestUpdateView.as_view(),
        name='pretest_update'
    ),

    url(
        '^(?P<course_pk>\d+)/create/$',
        views.PretestCreateView.as_view(),
        name='pretest_create'
    ),

    url(
        '^(?P<course_pk>\d+)/delete/(?P<pk>\d+)/$',
        views.PretestDeleteView.as_view(),
        name='pretest_delete'
    ),

    url(
        '^upload/(?P<pk>\d+)$',
        views.pretestfile_create,
        name='pretestfile_create'
    ),

    url(
        '^file/delete/(?P<pk>\d+)$',
        views.pretestfile_delete,
        name='pretestfile_delete'
    ),
]
