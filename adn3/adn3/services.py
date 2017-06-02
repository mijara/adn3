def is_student(user):
    return user.groups.filter(name='students').exists()


def is_teacher(user):
    return user.groups.filter(name='teachers').exists()


def is_assistant(user):
    return user.groups.filter(name='assistants').exists()