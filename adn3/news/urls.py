from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^(?P<pk>\d+)/$',
        views.index,
        name='index'
    ),

    url(
        '^show/(?P<pk>\d+)/$',
        views.show,
        name='show'
    ),

    url(
        '^create/(?P<course_pk>\d+)/$',
        views.create,
        name='create'
    ),
]
