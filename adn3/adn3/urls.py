from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from adn3 import settings

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
        '^classes/',
        include(
            'classes.urls',
            namespace='classes'
        )
    ),

    url(
        '^files/',
        include(
            'files.urls',
            namespace='files'
        )
    ),

    url(
        '^attendance/',
        include(
            'attendance.urls',
            namespace='attendance'
        )
    ),

    url(
        r'^admin/',
        include(
            admin.site.urls
        )
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
