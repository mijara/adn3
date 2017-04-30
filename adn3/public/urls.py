from django.conf.urls import url
import views

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
]
