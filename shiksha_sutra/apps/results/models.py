from django.db import models
from shiksha_sutra.apps.students.models import Student
from shiksha_sutra.apps.courses.models import Subject

class Exam(models.Model):
    EXAM_TYPES = (
        ('internal', 'Internal Assessment'),
        ('midterm', 'Mid Term'),
        ('final', 'Final Exam'),
    )
    
    name = models.CharField(max_length=100)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    max_marks = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.subject.name}"

class Result(models.Model):
    GRADE_CHOICES = (
        ('A+', 'A+ (90-100)'),
        ('A', 'A (80-89)'),
        ('B+', 'B+ (70-79)'),
        ('B', 'B (60-69)'),
        ('C+', 'C+ (50-59)'),
        ('C', 'C (40-49)'),
        ('F', 'F (Below 40)'),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['student', 'exam']
    
    def save(self, *args, **kwargs):
        # Auto-calculate grade based on marks
        percentage = (self.marks_obtained / self.exam.max_marks) * 100
        if percentage >= 90:
            self.grade = 'A+'
        elif percentage >= 80:
            self.grade = 'A'
        elif percentage >= 70:
            self.grade = 'B+'
        elif percentage >= 60:
            self.grade = 'B'
        elif percentage >= 50:
            self.grade = 'C+'
        elif percentage >= 40:
            self.grade = 'C'
        else:
            self.grade = 'F'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.exam.name} - {self.grade}"