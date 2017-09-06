from django.contrib import admin
from .models import FlyIn


class FlyInAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'course', 'software')


admin.site.register(FlyIn, FlyInAdmin)
