from django import forms
from django.contrib.auth.models import User
from .models import Faculty

class FacultyForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    
    class Meta:
        model = Faculty
        fields = ['employee_id', 'department', 'designation', 'qualification', 
                 'experience', 'phone', 'address', 'joining_date']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        if self.instance.pk:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            self.fields['username'].initial = self.instance.user.username
    
    def save(self, commit=True):
        faculty = super().save(commit=False)
        
        if not faculty.user_id:
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                password='faculty123'
            )
            faculty.user = user
        else:
            user = faculty.user
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.username = self.cleaned_data['username']
            user.save()
        
        if commit:
            faculty.save()
        return faculty