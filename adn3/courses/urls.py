from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^/$',
        views.index,
        name='index'
    ),

    url(
        '^show/(?P<pk>\d+)/$',
        views.show,
        name='show'
    ),

    url(
        '^grades/(?P<pk>\d+)/$',
        views.grades,
        name='grades'
    ),

    url(
        '^grades/(?P<pk>\d+)/config/$',
        views.grades_config,
        name='grades-config'
    ),
]
