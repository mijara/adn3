from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^(?P<course_pk>\d+)/create/$',
        views.PreRegistrationCreateView.as_view(),
        name='preregistration_create'
    ),

    url(
        '^detail/(?P<pk>\d+)/$',
        views.PreRegistrationDetailView.as_view(),
        name='preregistration_detail'
    ),

    url(
        '^$',
        views.CourseListView.as_view(),
        name='course_list'
    ),

    url(
        '^course/(?P<pk>\d+)/$',
        views.CourseDetailView.as_view(),
        name='course_detail'
    ),
]
