from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='list'),
    path('<int:pk>/', views.course_detail, name='detail'),
    path('create/', views.course_create, name='create'),
    path('<int:course_id>/add-subject/', views.subject_create, name='add_subject'),
]