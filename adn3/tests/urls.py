from django.conf.urls import url
import views

urlpatterns = [
    url(
        r'^(?P<course_pk>\d+)/$',
        views.TestList.as_view(),
        name='test_list'
    ),

    url(
        r'^detail/(?P<pk>\d+)/$',
        views.TestDetail.as_view(),
        name='test_detail'
    ),

    url(
        r'^(?P<course_pk>\d+)/create/$',
        views.TestCreate.as_view(),
        name='test_create'
    ),

    url(
        r'^(?P<course_pk>\d+)/update/(?P<pk>\d+)/$',
        views.TestUpdate.as_view(),
        name='test_update'
    ),

    url(
        r'^(?P<course_pk>\d+)/delete/(?P<pk>\d+)/$',
        views.TestDelete.as_view(),
        name='test_delete'
    ),

    url(
        r'^version/detail/(?P<pk>\d+)/$',
        views.VersionDetail.as_view(),
        name='version_detail'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/create/$',
        views.VersionCreate.as_view(),
        name='version_create'
    ),

    url(
        r'^(?P<test_pk>\d+)/version/delete/(?P<pk>\d+)/$',
        views.VersionDelete.as_view(),
        name='version_delete'
    ),

    url(
        r'^(?P<version_pk>\d+)/question/choice/create/$',
        views.ChoiceQuestionCreate.as_view(),
        name='choicequestion_create'
    ),

    url(
        r'^(?P<version_pk>\d+)/question/choice/update/(?P<pk>\d+)/$',
        views.ChoiceQuestionUpdate.as_view(),
        name='choicequestion_update'
    ),

    url(
        r'^(?P<version_pk>\d+)/question/choice/delete/(?P<pk>\d+)/$',
        views.ChoiceQuestionDelete.as_view(),
        name='choicequestion_delete'
    ),

    url(
        r'^(?P<version_pk>\d+)/question/text/create/$',
        views.TextQuestionCreate.as_view(),
        name='textquestion_create'
    ),

    url(
        r'^(?P<version_pk>\d+)/question/text/update/(?P<pk>\d+)/$',
        views.TextQuestionUpdate.as_view(),
        name='textquestion_update'
    ),

    url(
        r'^(?P<version_pk>\d+)/question/text/delete/(?P<pk>\d+)/$',
        views.TextQuestionDelete.as_view(),
        name='textquestion_delete'
    ),

    url(
        r'^(?P<version_pk>\d+)/question/numerical/create/$',
        views.NumericalQuestionCreate.as_view(),
        name='numericalquestion_create'
    ),

    url(
        r'^(?P<version_pk>\d+)/question/numerical/update/(?P<pk>\d+)/$',
        views.NumericalQuestionUpdate.as_view(),
        name='numericalquestion_update'
    ),

    url(
        r'^(?P<version_pk>\d+)/question/numerical/delete/(?P<pk>\d+)/$',
        views.NumericalQuestionDelete.as_view(),
        name='numericalquestion_delete'
    ),
]
