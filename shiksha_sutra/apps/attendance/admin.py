from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'date', 'status', 'marked_by']
    list_filter = ['status', 'date', 'subject']
    search_fields = ['student__user__first_name', 'student__user__last_name', 'subject__name']
    date_hierarchy = 'date'