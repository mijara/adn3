from django.contrib import admin
from .models import *


class PretestUploadAdmin(admin.ModelAdmin):
    search_fields = ('student__user__first_name', 'student__user__last_name', 'student__user__email')

    list_display = ('student', 'pretest', 'qualification')


admin.site.register(Pretest)
admin.site.register(PretestFile)
admin.site.register(PretestUpload, PretestUploadAdmin)
