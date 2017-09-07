from django import template

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_pretestupload(context, pretest):
    for pretestupload in pretest.pretestupload_set.all():
        if context['request'].user == pretestupload.student.user:
            return pretestupload
    return None