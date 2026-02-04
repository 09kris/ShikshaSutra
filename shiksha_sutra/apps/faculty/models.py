from django.db import models
from django.contrib.auth.models import User
from shiksha_sutra.apps.students.models import Department
from shiksha_sutra.apps.courses.models import Subject

class Faculty(models.Model):
    DESIGNATION_CHOICES = (
        ('professor', 'Professor'),
        ('associate_professor', 'Associate Professor'),
        ('assistant_professor', 'Assistant Professor'),
        ('lecturer', 'Lecturer'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30, choices=DESIGNATION_CHOICES)
    qualification = models.CharField(max_length=200)
    experience = models.IntegerField(help_text="Years of experience")
    phone = models.CharField(max_length=15)
    address = models.TextField()
    joining_date = models.DateField()
    
    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name()}"
    
    class Meta:
        verbose_name_plural = "Faculty"

class SubjectAssignment(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=10)
    
    class Meta:
        unique_together = ['faculty', 'subject', 'academic_year']
    
    def __str__(self):
        return f"{self.faculty.user.get_full_name()} - {self.subject.name}"