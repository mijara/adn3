from django.conf.urls import url
from . import views, pretest_views

urlpatterns = [
    url(
        '^(?P<pk>\d+)/$',
        views.CourseDetail.as_view(),
        name='course_detail'
    ),

    url(
        '^$',
        views.AgendaListView.as_view(),
        name='agenda_list'
    ),

    url(
        '^test/(?P<pk>\d+)/$',
        views.Test.as_view(),
        name="do_test"
    ),

    url(
        '^test/preconfirmation/(?P<pk>\d+)/$',
        views.PreconfirmationTest.as_view(),
        name="preconfirmation_test"
    ),

    url(
        '^test/assign/(?P<pk>\d+)/$',
        views.AssignTestVersion.as_view(),
        name="assign_test_version"
    ),

    url(
        '^test/update/$',
        views.UpdateAnswers.as_view(),
        name="update_answers"
    ),

    url(
        '^pretest/(?P<pk>\d+)/$',
        pretest_views.PretestDetailView.as_view(),
        name="pretest_detail"
    )
]
