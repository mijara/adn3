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
        views.TestDetailView.as_view(),
        name="test_detail"
    ),

    url(
        '^test/preconfirmation/(?P<pk>\d+)/$',
        views.TestPreConfirmationView.as_view(),
        name="test_preconfirmation"
    ),

    url(
        '^test/assign/(?P<pk>\d+)/$',
        views.TestVersionAssignView.as_view(),
        name="test_version_assign"
    ),

    url(
        '^test/update/$',
        views.UpdateAnswers.as_view(),
        name="update_answers"
    ),

    url(
        '^agenda/inscription/$',
        views.AgendaInscriptionView.as_view(),
        name="agenda_inscription"
    ),

    url(
        '^agenda/inscription/success$',
        views.AgendaInscriptionSuccessView.as_view(),
        name="agenda_inscription_success"
    ),

    url(
        '^agenda/information/(?P<code>[A-Za-z0-9]+)/$',
        views.AgendaInfoView.as_view(),
        name="agenda_information"
    ),

    url(
        '^pretest/(?P<pk>\d+)/$',
        pretest_views.PretestDetailView.as_view(),
        name="pretest_detail"
    ),

    url(
        '^pretest/(?P<pretest_pk>\d+)/upload/$',
        pretest_views.PretestUploadCreateView.as_view(),
        name="pretestupload_create"
    ),
]
