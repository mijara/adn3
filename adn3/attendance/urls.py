from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^show/(?P<agenda_pk>\d+)/$',
        views.show,
        name='show'
    ),

    url(
        '^save/(?P<agenda_pk>\d+)/$',
        views.save,
        name='save'
    ),
]
