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
        views.TeacherCreateSuccessView.as_view(),
        name='teacher_create_success'
    ),
]
