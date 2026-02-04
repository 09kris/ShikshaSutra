from django.urls import path
from . import views

app_name = 'faculty'

urlpatterns = [
    path('', views.faculty_list, name='list'),
    path('<int:pk>/', views.faculty_detail, name='detail'),
    path('create/', views.faculty_create, name='create'),
    path('<int:pk>/update/', views.faculty_update, name='update'),
]