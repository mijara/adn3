from django.contrib import admin
from .models import *


def fix_agendatest(modeladmin, request, queryset):
    for test in queryset.all():
        for agenda in test.course.agenda_set.all():
            print(test, agenda)

            if not AgendaTest.objects.filter(test=test, agenda=agenda).exists():
                AgendaTest.objects.create(agenda=agenda, test=test)
                print('created (agenda, test):', agenda, test)


fix_agendatest.short_description = "Fix legacy AgendaTest errors"


class ChoiceAnswerInline(admin.TabularInline):
    model = ChoiceAnswer


class ChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('version', 'text', 'score', 'html')
    inlines = (ChoiceAnswerInline,)


class NumericalAnswerInline(admin.TabularInline):
    model = NumericalAnswer


class NumericalQuestionAdmin(admin.ModelAdmin):
    list_display = ('version', 'text', 'score', 'html', 'top_limit', 'bottom_limit')
    inlines = (NumericalAnswerInline,)


class TextAnswerInline(admin.TabularInline):
    model = TextAnswer


class TextQuestionAdmin(admin.ModelAdmin):
    list_display = ('version', 'text', 'score', 'html')
    inlines = (TextAnswerInline,)


class VersionInline(admin.TabularInline):
    model = StudentsAnswers


class VersionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'create_date')
    inlines = (VersionInline,)


class AlternativeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'question', 'correct')


class StudentsAnswersAdmin(admin.ModelAdmin):
    search_fields = ('student__first_name', 'student__last_name', 'student__email')
    list_display = ('__str__', 'student', 'qualification', 'started_at')


class AgendaTestAdmin(admin.ModelAdmin):
    list_display = ('agenda', 'test', 'active')


class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'create_date')
    actions = [fix_agendatest]
    list_filter = ('course__year', 'course__semester')


admin.site.register(Test, TestAdmin)
admin.site.register(AgendaTest, AgendaTestAdmin)
admin.site.register(StudentsAnswers, StudentsAnswersAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(ChoiceQuestion, ChoiceQuestionAdmin)
admin.site.register(NumericalQuestion, NumericalQuestionAdmin)
admin.site.register(TextQuestion, TextQuestionAdmin)
admin.site.register(Alternative, AlternativeAdmin)
