from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^(?P<course_pk>\d+)/$',
        views.index,
        name='index'
    ),

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
]
