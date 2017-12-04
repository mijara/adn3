from django.conf.urls import url
from .views import PollCreateView, PollDetailView

urlpatterns = [
    url(
        '^create/$',
        PollCreateView.as_view(),
        name='poll_create'
    ),

    url(
        '^detail/(?P<pk>\d+)/$',
        PollDetailView.as_view(),
        name='poll_detail'
    ),
]
