from django.conf.urls import url
import views

urlpatterns = [
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
        '^upload/(?P<pk>\d+)$',
        views.upload,
        name='upload'
    ),
]
