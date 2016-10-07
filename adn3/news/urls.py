from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^show/(?P<pk>\d+)$',
        views.show,
        name='show'
    ),
]
