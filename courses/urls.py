from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^$',
        views.index,
        name='index'
    ),

    url(
        '^(?P<course_pk>\d+)/grades/$',
        views.GradesView.as_view(),
        name='course_grades'
    ),

    url(
        '^(?P<course_pk>\d+)/grades/excel/$',
        views.CourseGradesExcelView2.as_view(),
        name='course_grades_excel'
    ),

    url(
        '^(?P<course_pk>\d+)/grades/plain/$',
        views.CourseGradesExcelView2.as_view(),
        name='course_grades_excel_2'
    ),

    url(
        '^(?P<course_pk>\d+)/grades/config/$',
        views.GradesConfigView.as_view(),
        name='course_grades_config'
    ),

    url(
        '^(?P<course_pk>\d+)/students/excel/$',
        views.CourseStudentsExcelView.as_view(),
        name='course_students_excel'
    ),

    url(
        '^(?P<course_pk>\d+)/$',
        views.CourseDetail.as_view(),
        name='course_detail'
    ),

    url(
        '^(?P<course_pk>\d+)/(?P<section>.+)/$',
        views.CourseDetail.as_view(),
        name='course_detail'
    )
]
