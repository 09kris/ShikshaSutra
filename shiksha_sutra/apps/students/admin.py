from django.contrib import admin
from .models import Department, Student

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'description']
    search_fields = ['name', 'code']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'user', 'department', 'year', 'roll_number']
    list_filter = ['department', 'year', 'admission_date']
    search_fields = ['student_id', 'user__username', 'user__first_name', 'user__last_name']