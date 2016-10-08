from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^show/(?P<agenda_pk>\d+)/$',
        views.show,
        name='show'
    ),
]
