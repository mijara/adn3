from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^download/(?P<pk>\d+)/$',
        views.download,
        name='download'
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
]
