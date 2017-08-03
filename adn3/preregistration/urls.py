from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^(?P<course_pk>\d+)/create/$',
        views.PreRegistrationCreateView.as_view(),
        name='preregistration_create'
    ),

    url(
        '^(?P<course_pk>\d+)/news/$',
        views.NewListView.as_view(),
        name='new_list'
    ),

    url(
        '^(?P<pk>\d+)/detail/$',
        views.PreRegistrationDetailView.as_view(),
        name='preregistration_detail'
    ),

    url(
        '^(?P<pk>\d+)/delete/$',
        views.PreRegistrationDeleteView.as_view(),
        name='preregistration_delete'
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
