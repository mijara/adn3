from attendance.forms import AttendanceForm
from .models import *
from django.contrib.auth.models import User
import re

# format is: session, user
ZIP_FORMAT = r'(\d+)_(\d+).*'
ZIP_REGEX = re.compile(ZIP_FORMAT)


def unzip(value):
    """
    Assumes the value passed is always correct.

    :param value: value tu unzip.
    :return:
    """
    match = ZIP_REGEX.match(value)

    return int(match.group(1)), int(match.group(2))


def create_matrix(agenda):
    max_session_number = agenda.course.session_set.last().number

    table = []
    for user in agenda.inscriptions.all():
        records = user.attendance_set.filter(agenda=agenda.pk)
        row = []
        for i in range(1, max_session_number + 1):
            record = records.filter(session__number=i)

            prefix = '%s_%s' % (i, user.pk)

            if len(record) == 0:
                row.append(AttendanceForm(prefix=prefix))
            else:
                row.append(AttendanceForm(instance=record.first(), prefix=prefix))

        table.append([user, row])

    return table


def save_matrix(agenda, post):
    # filter all attendance fields.
    items = [p for p in post.items() if p[0].endswith('attended')]

    for key, attended in items:
        session_number, user_pk = unzip(key)
        session = agenda.course.session_set.filter(number=session_number).get()
        user = User.objects.get(pk=user_pk)

        try:
            attendance = Attendance.objects.get(agenda=agenda, session=session, user=user)
        except Attendance.DoesNotExist:
            attendance = Attendance(agenda=agenda, session=session, user=user)

        attendance.attended = attended
        attendance.save()
