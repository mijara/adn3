from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^(?P<pk>\d+)/$',
        views.CourseDetail.as_view(),
        name='course_detail'
    ),

    url(
        '^$',
        views.CourseList.as_view(),
        name='course_list'
    ),
    url(
      '^test/(?P<pk>\d+)/$',
        views.Test.as_view(),
        name="do_test"
    ),
]
