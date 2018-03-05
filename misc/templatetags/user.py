from django import template

from adn3 import services


register = template.Library()


@register.filter
def is_teacher(user):
    return services.is_teacher(user)


@register.filter
def is_student(user):
    return services.is_student(user)

@register.filter
def is_assistant(user):
    return services.is_assistant(user)


@register.filter
def is_coordinator(user):
    return services.is_coordinator(user)
