import re

from adn3.services import preregistrations_open, registrations_open


def constants(request):
    return {
        'PRE_REGISTRATIONS_OPEN': preregistrations_open(),
        'REGISTRATIONS_OPEN': registrations_open(),
    }


def url_args(request):
    match = re.match('^/([^/]*)', request.path)
    if match is None:
        active = ''
    else:
        active = match.group(1)

    return {
        'ACTIVE': active,
    }


def active_section(request):
    """
    Catches the current active section by matching:

    ^/\d+/([^/]*)

    For example:

    /1/news/... will catch "news"
    """
    match = re.match('^/\d+/([^/]*)', request.path)

    if match is None:
        active = ''
    else:
        active = match.group(1)

    return {
        'ACTIVE': active,
    }
