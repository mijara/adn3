from django.conf.urls import url
import views

urlpatterns = [
    url(
        '^$',
        views.CourseListView.as_view(),
        name='index'
    ),
]
