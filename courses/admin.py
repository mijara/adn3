from django.contrib import admin
from .models import *


class CourseTeacherInline(admin.TabularInline):
    model = CourseTeacher


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'campus', 'year', 'semester', 'status')
    inlines = (CourseTeacherInline,)


class AgendaAdmin(admin.ModelAdmin):
    list_display = ('day', 'block', 'room_name', 'course_name', 'campus', 'software')

    def room_name(self, object):
        return object.room.name

    def course_name(self, object):
        return object.course.name

    def campus(self, object):
        return object.course.campus.name


admin.site.register(Room)
admin.site.register(Campus)
admin.site.register(Course, CourseAdmin)
admin.site.register(Agenda, AgendaAdmin)
