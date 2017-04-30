from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^(?P<course_pk>\d+)/create/$',
        views.PreRegistrationCreateView.as_view(),
        name='preregistration_create'
    ),
    url(
        '^(?P<pk>\d+)/$',
        views.CoursePreRegistrationDetailView.as_view(),
        name='course_detail'
    ),
]
