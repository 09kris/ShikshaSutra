from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student, Department
from .forms import StudentForm

@login_required
def student_list(request):
    students = Student.objects.all().select_related('user', 'department')
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'students/list.html', {'page_obj': page_obj})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'student': student})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully!')
            return redirect('students:list')
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form, 'title': 'Add Student'})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('students:detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/form.html', {'form': form, 'title': 'Update Student'})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('students:list')
    return render(request, 'students/delete.html', {'student': student})