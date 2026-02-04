from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Exam, Result
from .forms import ExamForm, ResultForm
from shiksha_sutra.apps.students.models import Student

@login_required
def exam_list(request):
    exams = Exam.objects.all().select_related('subject')
    return render(request, 'results/exam_list.html', {'exams': exams})

@login_required
def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exam created successfully!')
            return redirect('results:exam_list')
    else:
        form = ExamForm()
    return render(request, 'results/exam_form.html', {'form': form})

@login_required
def add_result(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    students = Student.objects.filter(department=exam.subject.course.department)
    
    if request.method == 'POST':
        for student in students:
            marks = request.POST.get(f'marks_{student.id}')
            if marks:
                result, created = Result.objects.get_or_create(
                    student=student,
                    exam=exam,
                    defaults={'marks_obtained': int(marks)}
                )
                if not created:
                    result.marks_obtained = int(marks)
                    result.save()
        
        messages.success(request, 'Results added successfully!')
        return redirect('results:exam_list')
    
    return render(request, 'results/add_result.html', {'exam': exam, 'students': students})

@login_required
def student_results(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    results = Result.objects.filter(student=student).select_related('exam', 'exam__subject')
    return render(request, 'results/student_results.html', {'student': student, 'results': results})

@login_required
def result_report(request):
    results = Result.objects.all().select_related('student', 'exam')
    return render(request, 'results/report.html', {'results': results})