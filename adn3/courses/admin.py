from django.contrib import admin
from models import *


class CourseTeacherInline(admin.TabularInline):
    model = CourseTeacher


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'campus', 'year', 'semester', 'status')
    inlines = (CourseTeacherInline,)


admin.site.register(Room)
admin.site.register(Campus)
admin.site.register(Course, CourseAdmin)
admin.site.register(Agenda)
