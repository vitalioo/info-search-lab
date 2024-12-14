from django import forms
from .models import University, Student

class UniversityForm(forms.ModelForm):
    established_date = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=['%d.%m.%Y', '%Y-%m-%d']
    )

    class Meta:
        model = University
        fields = '__all__'

class StudentForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=['%d.%m.%Y', '%Y-%m-%d']
    )

    class Meta:
        model = Student
        fields = '__all__'