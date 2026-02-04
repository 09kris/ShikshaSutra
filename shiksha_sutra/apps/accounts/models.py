from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    USER_TYPES = (
        ('admin', 'Administrator'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"