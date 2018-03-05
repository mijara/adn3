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
        r'^students/create/$',
        views.StudentCreateView.as_view(),
        name='student_create'
    ),

    url(
        r'^students/success/$',
        views.StudentSuccessView.as_view(),
        name='student_success'
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

    url(
        r'^yearsemester/update/$',
        views.YearSemesterUpdateView.as_view(),
        name='yearsemester_update'
    ),

    url(
        r'^teacher-course/create/$',
        views.TeacherCourseCreateView.as_view(),
        name='teacher_course_create'
    ),

    url(
        r'^coassistant-course/create/$',
        views.CoAssistantCourseCreateView.as_view(),
        name='co_assistant_course_create'
    ),

    url(
        r'^assistant-course/select/$',
        views.AssistantCourseSelectView.as_view(),
        name='assistant_course_select'
    ),

    url(
        r'^assistant-course/create/(?P<course_pk>\d+)/$',
        views.AssistantCourseCreateView.as_view(),
        name='assistant_course_create'
    ),

    url(
        r'^assistant/create/$',
        views.AssistantCreateView.as_view(),
        name='assistant_create'
    ),
]
