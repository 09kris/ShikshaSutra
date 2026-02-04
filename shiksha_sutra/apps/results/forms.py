from django import forms
from .models import Exam, Result

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name', 'exam_type', 'subject', 'date', 'max_marks']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'exam', 'marks_obtained']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})