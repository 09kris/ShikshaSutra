from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/create/', views.exam_create, name='exam_create'),
    path('exams/<int:exam_id>/add-result/', views.add_result, name='add_result'),
    path('student/<int:student_id>/', views.student_results, name='student_results'),
    path('report/', views.result_report, name='report'),
]