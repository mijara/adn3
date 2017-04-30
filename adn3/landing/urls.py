from django.conf.urls import url
import views

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
        '^logout/$',
        views.log_out,
        name='logout'
    ),
]
