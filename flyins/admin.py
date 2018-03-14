from django.contrib import admin
from .models import FlyIn


class FlyInAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'rol', 'course', 'software')
    search_fields = ('first_name', 'last_names', 'rol')


admin.site.register(FlyIn, FlyInAdmin)
