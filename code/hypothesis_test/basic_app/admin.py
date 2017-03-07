from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = (
        'name',
        'class_enrolled',
        'preferred_subject',
        'marks_obtained',)
    search_fields = ('name', 'class_enrolled')
    list_filter = (
        'name',)

admin.site.register(Student, StudentAdmin)
