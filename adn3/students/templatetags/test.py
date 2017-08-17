from django import template
from tests.models import StudentsAnswers
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


# Check test status
# 0: The test has not been performed
# 1: The test is in progress
# 2: The test is over
@register.simple_tag(takes_context=True)
def print_status(context, test):
    try:
        sv = StudentsAnswers.objects.get(student=context['request'].user, version__test=test)
        if sv.get_status() == 1:
            return '<span class="text-success">En curso</span>'
        elif sv.get_status() == 2:
            return '<span class="text-danger">Finalizado</span>'
    except ObjectDoesNotExist:
        return '<span class="text-muted">Pendiente</span>'

@register.assignment_tag(takes_context=True)
def get_status_code(context, test):
    try:
        sv = StudentsAnswers.objects.get(student=context['request'].user, version__test=test)
        return sv.get_status()
    except ObjectDoesNotExist:
        return 0

@register.simple_tag(takes_context=True)
def has_tests_to_show(context, agenda):
    for agendatest in agenda.agendatest_set.all():
        if agendatest.active and get_status_code(context, agendatest.test) != 2:
            return True
    return False

