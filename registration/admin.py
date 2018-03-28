from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    search_fields = ('user__first_name', 'user__email', 'rol')

    list_display = ('user', 'email', 'rol', 'campus')

    def email(self, obj):
        return obj.user.email


admin.site.register(Student, StudentAdmin)
admin.site.register(Ticket)
