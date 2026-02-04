from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    YEAR_CHOICES = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.CharField(max_length=1, choices=YEAR_CHOICES)
    roll_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    admission_date = models.DateField()
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    address = models.TextField()
    
    def __str__(self):
        return f"{self.student_id} - {self.user.get_full_name()}"
    
    class Meta:
        ordering = ['student_id']