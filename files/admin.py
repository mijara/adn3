from django.contrib import admin
from .models import *


class CourseFileDownloadAdmin(admin.ModelAdmin):
    fields = ('file', 'user')
    list_display = ('file', 'user', 'course')

    def course(self, object):
        return object.file.course


admin.site.register(CourseFile)
admin.site.register(CourseFileDownload, CourseFileDownloadAdmin)
