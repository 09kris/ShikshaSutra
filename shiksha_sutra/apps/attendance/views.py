from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from datetime import date
from .models import Attendance
from .forms import AttendanceForm
from shiksha_sutra.apps.students.models import Student
from shiksha_sutra.apps.courses.models import Subject

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            attendance_date = form.cleaned_data['date']
            students = Student.objects.filter(department=subject.course.department)
            
            for student in students:
                status = request.POST.get(f'student_{student.id}')
                if status:
                    attendance, created = Attendance.objects.get_or_create(
                        student=student,
                        subject=subject,
                        date=attendance_date,
                        defaults={'status': status, 'marked_by': request.user}
                    )
                    if not created:
                        attendance.status = status
                        attendance.save()
            
            messages.success(request, 'Attendance marked successfully!')
            return redirect('attendance:mark')
    else:
        form = AttendanceForm()
    
    return render(request, 'attendance/mark.html', {'form': form})

@login_required
def attendance_report(request):
    students = Student.objects.all()
    attendance_data = []
    
    for student in students:
        total_classes = Attendance.objects.filter(student=student).count()
        present_classes = Attendance.objects.filter(student=student, status='present').count()
        percentage = (present_classes / total_classes * 100) if total_classes > 0 else 0
        
        attendance_data.append({
            'student': student,
            'total_classes': total_classes,
            'present_classes': present_classes,
            'percentage': round(percentage, 2)
        })
    
    return render(request, 'attendance/report.html', {'attendance_data': attendance_data})

@login_required
def student_attendance(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    attendance_records = Attendance.objects.filter(student=student).select_related('subject')
    return render(request, 'attendance/student_detail.html', {
        'student': student,
        'attendance_records': attendance_records
    })