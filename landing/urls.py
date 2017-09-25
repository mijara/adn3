from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        '^$',
        views.index,
        name='index'
    ),

    url(
        '^sign-in/$',
        views.sign_in,
        name='sign_in'
    ),

    url(
        '^sign-in/(?P<err_code>.+)/$',
        views.sign_in,
        name='sign_in'
    ),

    url(
        '^logout/$',
        views.log_out,
        name='logout'
    ),
]
