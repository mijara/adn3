from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.AdministrationIndexView.as_view(),
        name='administration_index'
    ),

    url(
        r'^teachers/create/$',
        views.TeacherCreateView.as_view(),
        name='teacher_create'
    ),

    url(
        r'^teachers/create/success/$',
        views.TeacherSuccessView.as_view(),
        name='teacher_success'
    ),

    url(
        r'^courses/create/$',
        views.CourseCreateView.as_view(),
        name='course_create'
    ),

    url(
        r'^courses/create/success/$',
        views.CourseSuccessView.as_view(),
        name='course_success'
    ),
]
