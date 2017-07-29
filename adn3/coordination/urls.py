from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'$',
        views.CoordinationIndexView.as_view(),
        name='coordination_index'
    )
]
