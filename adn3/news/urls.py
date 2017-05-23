from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^detail/(?P<pk>\d+)/$',
        views.NewDetail.as_view(),
        name='new_detail'
    ),

    url(
        '^(?P<course_pk>\d+)/create/$',
        views.NewCreate.as_view(),
        name='new_create'
    ),

    url(
        '^(?P<course_pk>\d+)/update/(?P<pk>\d+)/$',
        views.NewUpdate.as_view(),
        name='new_update'
    ),

    url(
        '^(?P<course_pk>\d+)/delete/(?P<pk>\d+)/$',
        views.NewDelete.as_view(),
        name='new_delete'
    ),
]
