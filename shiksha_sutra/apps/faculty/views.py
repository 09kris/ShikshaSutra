from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Faculty, SubjectAssignment
from .forms import FacultyForm

@login_required
def faculty_list(request):
    faculty_members = Faculty.objects.all().select_related('user', 'department')
    return render(request, 'faculty/list.html', {'faculty_members': faculty_members})

@login_required
def faculty_detail(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    assignments = SubjectAssignment.objects.filter(faculty=faculty).select_related('subject')
    return render(request, 'faculty/detail.html', {'faculty': faculty, 'assignments': assignments})

@login_required
def faculty_create(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Faculty member created successfully!')
            return redirect('faculty:list')
    else:
        form = FacultyForm()
    return render(request, 'faculty/form.html', {'form': form, 'title': 'Add Faculty'})

@login_required
def faculty_update(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            messages.success(request, 'Faculty member updated successfully!')
            return redirect('faculty:detail', pk=faculty.pk)
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'faculty/form.html', {'form': form, 'title': 'Update Faculty'})