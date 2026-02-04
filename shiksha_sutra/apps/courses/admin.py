from django.contrib import admin
from .models import Course, Subject

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'department', 'semester', 'credits']
    list_filter = ['department', 'semester']
    search_fields = ['name', 'code']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'course', 'credits']
    list_filter = ['course__department']
    search_fields = ['name', 'code']