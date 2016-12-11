from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^(?P<pk>\d+)/$',
        views.SessionDetailView.as_view(),
        name='session_detail'
    ),

    url(
        '^(?P<course_pk>\d+)/create/$',
        views.SessionCreateView.as_view(),
        name='session_create'
    ),

    url(
        '^(?P<course_pk>\d+)/update/(?P<pk>\d+)/$',
        views.SessionUpdateView.as_view(),
        name='session_update'
    ),

    url(
        '^(?P<course_pk>\d+)/delete/(?P<pk>\d+)/$',
        views.SessionDeleteView.as_view(),
        name='session_delete'
    ),

    url(
        '^upload/(?P<pk>\d+)$',
        views.upload,
        name='upload'
    ),

    url(
        '^remove-file/(?P<file_pk>\d+)$',
        views.remove_file,
        name='remove_file'
    ),
]
