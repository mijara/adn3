from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^(?P<pk>\d+)/$',
        views.CourseFileDetailView.as_view(),
        name='coursefile_detail'
    ),

    url(
        '^download/(?P<pk>\d+)/$',
        views.download,
        name='coursefile_download'
    ),

    url(
        '^(?P<course_pk>\d+)/create/$',
        views.CourseFileCreateView.as_view(),
        name='coursefile_create'
    ),

    url(
        '^(?P<course_pk>\d+)/delete/(?P<pk>\d+)/$',
        views.CourseFileDeleteView.as_view(),
        name='coursefile_delete'
    ),

    url(
        '^(?P<course_pk>\d+)/update/(?P<pk>\d+)/$',
        views.CourseFileUpdateView.as_view(),
        name='coursefile_update'
    ),
]
