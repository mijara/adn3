from django import template

from adn3 import services
register = template.Library()


@register.filter
def is_teacher(user):
    return services.is_teacher(user)


@register.filter
def is_student(user):
    return services.is_student(user)