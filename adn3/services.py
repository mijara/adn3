from misc.models import Setting


def is_student(user):
    return user.groups.filter(name='students').exists()


def is_student_of(user, course):
    for agenda in course.agenda_set.all():
        if user in agenda.inscriptions.all():
            return True
    return False


def is_teacher(user):
    return user.groups.filter(name='teachers').exists()


def is_coordinator(user):
    return user.groups.filter(name='coordinators').exists()


def is_assistant(user):
    return user.groups.filter(name='assistants').exists()


def is_assistant_of(user, course):
    for agenda in course.agenda_set.all():
        if user in agenda.assistants.all():
            return True
    return False


def is_assistant_of_agenda(user, agenda):
    return user in agenda.assistants.all()


def preregistrations_open():
    try:
        return Setting.objects.get(key='preregistrations-open').get_bool()
    except:
        return False


def registrations_open():
    try:
        return Setting.objects.get(key='registrations-open').get_bool()
    except:
        return False


def welcome_message():
    return Setting.objects.get(key='welcome-message').get_str()


def preregistrations_set(value):
    obj = Setting.objects.get(key='preregistrations-open')
    obj.value = str(value)
    obj.save()


def registrations_set(value):
    obj = Setting.objects.get(key='registrations-open')
    obj.value = str(value)
    obj.save()


def is_teacher_of(user, course):
    return course.teachers.filter(pk=user.pk).exists()


def polls_open():
    try:
        return Setting.objects.get(key='polls-open').get_bool()
    except:
        return False

def polls_set(value):
    obj = Setting.objects.get(key='polls-open')
    obj.value = str(value)
    obj.save()
