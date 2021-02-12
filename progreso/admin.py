from django.contrib import admin
from .models import Date
# Register your models here.

class DateAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Date, DateAdmin)

