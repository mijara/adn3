from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'rol')

    list_display = ('full_name', 'email', 'rol', 'campus')

    def email(self, obj):
        return obj.user.email

    def full_name(self, obj):
        return obj.user.get_full_name()


admin.site.register(Student, StudentAdmin)
admin.site.register(Ticket)
