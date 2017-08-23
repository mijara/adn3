from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^(?P<pk>\d+)/$',
        views.CourseFileDetailView.as_view(),
        name='coursefile_detail'
    ),

    url(
        '^(?P<pk>\d+)/download/$',
        views.download,
        name='coursefile_download'
    ),

    url(
        '^create/$',
        views.CourseFileCreateView.as_view(),
        name='coursefile_create'
    ),

    url(
        '^(?P<pk>\d+)/delete/$',
        views.CourseFileDeleteView.as_view(),
        name='coursefile_delete'
    ),

    url(
        '^(?P<pk>\d+)/update/$',
        views.CourseFileUpdateView.as_view(),
        name='coursefile_update'
    ),
]
