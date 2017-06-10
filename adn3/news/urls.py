from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^detail/(?P<pk>\d+)/$',
        views.NewDetail.as_view(),
        name='new_detail'
    ),

    url(
        '^create/$',
        views.NewCreate.as_view(),
        name='new_create'
    ),

    url(
        '^update/(?P<pk>\d+)/$',
        views.NewUpdate.as_view(),
        name='new_update'
    ),

    url(
        '^delete/(?P<pk>\d+)/$',
        views.NewDelete.as_view(),
        name='new_delete'
    ),
]
