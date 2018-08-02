from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^show-duplicates/$',
        views.ShowDuplicatesView.as_view(),
        name='index'
    ),
]
