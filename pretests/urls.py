from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^(?P<pk>\d+)/$',
        views.PretestDetailView.as_view(),
        name='pretest_detail'
    ),

    url(
        '^(?P<pk>\d+)/update/$',
        views.PretestUpdateView.as_view(),
        name='pretest_update'
    ),

    url(
        '^create/$',
        views.PretestCreateView.as_view(),
        name='pretest_create'
    ),

    url(
        '^(?P<pk>\d+)/delete/$',
        views.PretestDeleteView.as_view(),
        name='pretest_delete'
    ),

    url(
        '^(?P<pretest_pk>\d+)/file/upload/$',
        views.PretestFileCreateView.as_view(),
        name='pretestfile_create'
    ),

    url(
        '^(?P<pretest_pk>\d+)/file/(?P<pk>\d+)/delete/$',
        views.PretestFileDeleteView.as_view(),
        name='pretestfile_delete'
    ),

    url(
        r'^(?P<pk>\d+)/review/$',
        views.PretestReviewListView.as_view(),
        name='pretest_review_list'
    ),

    url(
        r'^(?P<pretest_pk>\d+)/review/(?P<pk>\d+)$',
        views.PretestReviewView.as_view(),
        name='pretest_review'
    ),
]
