from django.contrib import admin
from .models import *


class PreRegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'software')
    list_filter = ('course', 'software')


# Deprecated.
# admin.site.register(PreRegistration, PreRegistrationAdmin)
