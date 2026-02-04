from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark'),
    path('report/', views.attendance_report, name='report'),
    path('student/<int:student_id>/', views.student_attendance, name='student_detail'),
]