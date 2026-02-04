from django.contrib import admin
from .models import Faculty, SubjectAssignment

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'user', 'department', 'designation']
    list_filter = ['department', 'designation']
    search_fields = ['employee_id', 'user__username', 'user__first_name', 'user__last_name']

@admin.register(SubjectAssignment)
class SubjectAssignmentAdmin(admin.ModelAdmin):
    list_display = ['faculty', 'subject', 'academic_year']
    list_filter = ['academic_year', 'subject__course__department']