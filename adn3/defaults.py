# coding=utf-8
from django.forms import Field
from django.utils.translation import ugettext_lazy

Field.default_error_messages = {
    'required': ugettext_lazy(u'Este campo es requerido.'),
    'invalid': ugettext_lazy(u'Ingrese un valor válido.'),
}
