from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(
        '^',
        include(
            'landing.urls',
            namespace='landing'
        )
    ),

    url(
        '^self/',
        include(
            'self.urls',
            namespace='self'
        )
    ),

    url(
        '^courses/',
        include(
            'courses.urls',
            namespace='courses'
        )
    ),

    url(
        '^news/',
        include(
            'news.urls',
            namespace='news'
        )
    ),

    url(
        r'^admin/',
        include(
            admin.site.urls
        )
    ),
]
