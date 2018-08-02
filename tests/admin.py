from django.contrib import admin
from .models import *


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


admin.site.register(Test)
admin.site.register(AgendaTest, AgendaTestAdmin)
admin.site.register(StudentsAnswers, StudentsAnswersAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(ChoiceQuestion, ChoiceQuestionAdmin)
admin.site.register(NumericalQuestion, NumericalQuestionAdmin)
admin.site.register(TextQuestion, TextQuestionAdmin)
admin.site.register(Alternative, AlternativeAdmin)
