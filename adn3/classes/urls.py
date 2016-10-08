from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^(?P<course_pk>\d+)/$',
        views.index,
        name='index'
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
