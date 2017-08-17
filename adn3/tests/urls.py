from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        views.TestDetail.as_view(),
        name='test_detail'
    ),

    url(
        r'^create/$',
        views.TestCreate.as_view(),
        name='test_create'
    ),

    url(
        r'^(?P<pk>\d+)/review/$',
        views.TestReviewListView.as_view(),
        name='test_review_list'
    ),

    url(
        r'^(?P<test_pk>\d+)/review/(?P<pk>\d+)$',
        views.TestReviewView.as_view(),
        name='test_review'
    ),

    url(
        r'^(?P<test_pk>\d+)/download/(?P<pk>\d+)$',
        views.DownloadStudentFileView.as_view(),
        name='download_student_file'
    ),

    url(
        r'^(?P<pk>\d+)/update/$',
        views.TestUpdate.as_view(),
        name='test_update'
    ),

    url(
        r'^(?P<pk>\d+)/delete/$',
        views.TestDelete.as_view(),
        name='test_delete'
    ),

    url(
        r'^(?P<pk>\d+)/toggle/(?P<agenda_pk>\d+)/(?P<referrer>.+)/$',
        views.ToggleTest.as_view(),
        name="toggle_test"
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<pk>\d+)/detail/$',
        views.VersionDetail.as_view(),
        name='version_detail'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/create/$',
        views.VersionCreate.as_view(),
        name='version_create'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<pk>\d+)/delete/$',
        views.VersionDelete.as_view(),
        name='version_delete'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<pk>\d+)/duplicate/$',
        views.VersionDuplicateView.as_view(),
        name='version_duplicate'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<version_pk>\d+)/attachfile/$',
        views.version_attach_file,
        name='version_attach_file'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<version_pk>\d+)/question/choice/create/$',
        views.ChoiceQuestionCreate.as_view(),
        name='choicequestion_create'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<version_pk>\d+)/question/choice/(?P<pk>\d+)/update/$',
        views.ChoiceQuestionUpdate.as_view(),
        name='choicequestion_update'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<version_pk>\d+)/question/choice/(?P<pk>\d+)/delete/$',
        views.ChoiceQuestionDelete.as_view(),
        name='choicequestion_delete'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<version_pk>\d+)/question/text/create/$',
        views.TextQuestionCreate.as_view(),
        name='textquestion_create'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<version_pk>\d+)/question/text/(?P<pk>\d+)/update/$',
        views.TextQuestionUpdate.as_view(),
        name='textquestion_update'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<version_pk>\d+)/question/text/(?P<pk>\d+)/delete/$',
        views.TextQuestionDelete.as_view(),
        name='textquestion_delete'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<version_pk>\d+)/question/numerical/create/$',
        views.NumericalQuestionCreate.as_view(),
        name='numericalquestion_create'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<version_pk>\d+)/question/numerical/(?P<pk>\d+)/update/$',
        views.NumericalQuestionUpdate.as_view(),
        name='numericalquestion_update'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/(?P<version_pk>\d+)/question/numerical/(?P<pk>\d+)/delete/$',
        views.NumericalQuestionDelete.as_view(),
        name='numericalquestion_delete'
    ),
]
