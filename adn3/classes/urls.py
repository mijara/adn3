from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^(?P<course_pk>\d+)/$',
        views.index,
        name='index'
    ),

    url(
        '^show/(?P<pk>\d+)/$',
        views.show,
        name='show'
    ),

    url(
        '^(?P<course_pk>\d+)/create/$',
        views.detail,
        name='create'
    ),

    url(
        '^(?P<course_pk>\d+)/edit/(?P<pk>\d+)$',
        views.detail,
        name='edit'
    ),

    url(
        '^upload/(?P<session_pk>\d+)$',
        views.upload,
        name='upload'
    ),

    url(
        '^remove-file/(?P<file_pk>\d+)$',
        views.remove_file,
        name='remove_file'
    ),
]
