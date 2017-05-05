import re

from constants import *


def constants(request):
    return {
        'PRE_REGISTRATIONS_OPEN': PRE_REGISTRATIONS_OPEN,
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
