from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^$',
        views.index,
        name='index'
    ),

    url(
        '^show/(?P<pk>\d+)$',
        views.show,
        name='show'
    ),
]
