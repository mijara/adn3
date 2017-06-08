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
        '^(?P<course_pk>\d+)/news/',
        include(
            'news.urls',
            namespace='news'
        )
    ),

    url(
        '^(?P<course_pk>\d+)/sessions/',
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
        '^pretests/',
        include(
            'pretests.urls',
            namespace='pretests'
        )
    ),

    url(
        '^tests/',
        include(
            'tests.urls',
            namespace='tests'
        )
    ),

    url(
        '^public/',
        include(
            'public.urls',
            namespace='public'
        )
    ),

    url(
        '^preregistrations/',
        include(
            'preregistration.urls',
            namespace='preregistrations'
        )
    ),

    url(
        '^students/',
        include(
            'students.urls',
            namespace='students'
        )
    ),

    url(
        r'^admin/',
        include(
            admin.site.urls
        )
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
