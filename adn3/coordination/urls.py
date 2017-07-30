from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.CoordinationIndexView.as_view(),
        name='coordination_index'
    ),

    url(
        r'^preregistrations/excel/$',
        views.PreRegistrationExcelView.as_view(),
        name='preregistrations_excel'
    ),
]
