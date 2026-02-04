from django import forms
from datetime import date
from .models import Attendance
from shiksha_sutra.apps.courses.models import Subject

class AttendanceForm(forms.Form):
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date = forms.DateField(
        initial=date.today,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )