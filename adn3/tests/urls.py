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
]
