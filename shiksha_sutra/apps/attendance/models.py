from django.db import models
from django.contrib.auth.models import User
from shiksha_sutra.apps.students.models import Student
from shiksha_sutra.apps.courses.models import Subject

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    marked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['student', 'subject', 'date']
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.subject.name} - {self.date}"