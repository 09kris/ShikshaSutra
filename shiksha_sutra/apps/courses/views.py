from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Subject
from .forms import CourseForm, SubjectForm

@login_required
def course_list(request):
    courses = Course.objects.all().select_related('department')
    return render(request, 'courses/list.html', {'courses': courses})

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    subjects = course.subjects.all()
    return render(request, 'courses/detail.html', {'course': course, 'subjects': subjects})

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course created successfully!')
            return redirect('courses:list')
    else:
        form = CourseForm()
    return render(request, 'courses/form.html', {'form': form, 'title': 'Add Course'})

@login_required
def subject_create(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.course = course
            subject.save()
            messages.success(request, 'Subject added successfully!')
            return redirect('courses:detail', pk=course.pk)
    else:
        form = SubjectForm()
    return render(request, 'courses/subject_form.html', {'form': form, 'course': course})