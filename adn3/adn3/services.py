from misc.models import Setting


def is_student(user):
    return user.groups.filter(name='students').exists()


def is_teacher(user):
    return user.groups.filter(name='teachers').exists()


def is_coordinator(user):
    return user.groups.filter(name='coordinators').exists()


def is_assistant(user):
    return user.groups.filter(name='assistants').exists()


def is_assistant_of(user, agenda):
    return user in agenda.assistants.all()


def preregistrations_open():
    return Setting.objects.get(key='preregistrations-open').get_bool()


def is_teacher_of(user, course):
    return course.teachers.filter(pk=user.pk).exists()
