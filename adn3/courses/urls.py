from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^$',
        views.index,
        name='index'
    ),

    url(
        '^detail/(?P<course_pk>\d+)/$',
        views.CourseDetail.as_view(),
        name='course_detail'
    ),

    url(
        '^detail/(?P<course_pk>\d+)/(?P<section>.+)/$',
        views.CourseDetail.as_view(),
        name='course_detail'
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
