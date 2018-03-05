from django.core.urlresolvers import reverse
from django import template


register = template.Library()


@register.filter
def admin_url(instance):
    info = (instance._meta.app_label, instance._meta.model_name)
    return reverse('admin:%s_%s_change' % info, args=(instance.pk,))
