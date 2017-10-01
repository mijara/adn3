from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^$',
        views.CourseListView.as_view(),
        name='course_list'
    ),

    url(
        '^(?P<pk>\d+)/$',
        views.CourseDetailView.as_view(),
        name='course_detail'
    ),
]
