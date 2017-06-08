from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^(?P<pk>\d+)/$',
        views.SessionDetailView.as_view(),
        name='session_detail'
    ),

    url(
        '^create/$',
        views.SessionCreateView.as_view(),
        name='session_create'
    ),

    url(
        '^(?P<pk>\d+)/update/$',
        views.SessionUpdateView.as_view(),
        name='session_update'
    ),

    url(
        '^(?P<pk>\d+)/delete/$',
        views.SessionDeleteView.as_view(),
        name='session_delete'
    ),

    url(
        '^(?P<session_pk>\d+)/file/create/$',
        views.SessionFileCreateView.as_view(),
        name='sessionfile_create'
    ),

    url(
        '^(?P<session_pk>\d+)/file/delete/(?P<pk>\d+)$',
        views.SessionFileDeleteView.as_view(),
        name='sessionfile_delete'
    ),
]
