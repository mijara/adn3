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
        '^teachers/',
        include(
            'teachers.urls',
            namespace='teachers'
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
        '^(?P<course_pk>\d+)/files/',
        include(
            'files.urls',
            namespace='files'
        )
    ),

    url(
        '^(?P<course_pk>\d+)/attendance/',
        include(
            'attendance.urls',
            namespace='attendance'
        )
    ),

    url(
        '^(?P<course_pk>\d+)/pretests/',
        include(
            'pretests.urls',
            namespace='pretests'
        )
    ),

    url(
        '^(?P<course_pk>\d+)/tests/',
        include(
            'tests.urls',
            namespace='tests'
        )
    ),

    url(
        r'^(?P<course_pk>\d+)/polls/',
        include(
            'polls.urls',
            namespace='polls'
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
        '^flyins/',
        include(
            'flyins.urls',
            namespace='flyins'
        )
    ),

    url(
        '^registration/',
        include(
            'registration.urls',
            namespace='registration'
        )
    ),

    url(
        '^coordination/',
        include(
            'coordination.urls',
            namespace='coordination'
        )
    ),

    url(
        r'^admin/',
        include(
            admin.site.urls
        )
    ),

    url(
        r'^assistants/',
        include(
            'assistants.urls',
            namespace='assistants'
        )
    ),

    url(
        r'^public/',
        include(
            'public.urls',
            namespace='public'
        )
    ),

    url(
        r'^administration/',
        include(
            'administration.urls',
            namespace='administration'
        )
    ),

    url(
      r'^playground/',
      include(
          'playground.urls',
          namespace='playground'
      )
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
