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
]
