from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^$',
        views.CourseListView.as_view(),
        name='course_list'
    ),
    
    url(
        '^(?P<course_pk>\d+)/create/$',
        views.FlyInCreateView.as_view(),
        name='preregistration_create'
    ),

    url(
        '^(?P<course_pk>\d+)/news/$',
        views.NewListView.as_view(),
        name='new_list'
    ),

    url(
        '^(?P<pk>\d+)/detail/$',
        views.FlyInDetailView.as_view(),
        name='preregistration_detail'
    ),
]
