from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^(?P<pk>\d+)/$',
        views.CoursePreRegistrationDetailView.as_view(),
        name='course_detail'
    ),
]
