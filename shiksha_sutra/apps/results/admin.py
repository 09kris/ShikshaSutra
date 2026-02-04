from django.contrib import admin
from .models import Exam, Result

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam_type', 'subject', 'date', 'max_marks']
    list_filter = ['exam_type', 'date', 'subject__course__department']
    search_fields = ['name', 'subject__name']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'exam', 'marks_obtained', 'grade']
    list_filter = ['grade', 'exam__exam_type']
    search_fields = ['student__user__first_name', 'student__user__last_name', 'exam__name']