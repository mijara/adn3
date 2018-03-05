from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^$',
        views.CourseListView.as_view(),
        name='index'
    ),

    url(
        '^update-password/$',
        views.TeacherPasswordUpdateView.as_view(),
        name='teacher_password_update'
    ),
]
