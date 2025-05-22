from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'program', 'course', 'group_number', 'specialization', 'graduation_year', 'average_grade']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Введите ФИО'}),
            'program': forms.TextInput(attrs={'placeholder': 'Введите образовательную программу'}),
            'course': forms.Select(),
            'group_number': forms.TextInput(attrs={'placeholder': 'Введите номер группы'}),
            'specialization': forms.Select(),
            'graduation_year': forms.NumberInput(attrs={'placeholder': 'Введите год окончания'}),
            'average_grade': forms.NumberInput(attrs={'step': '0.1', 'min': '0', 'max': '10', 'placeholder': 'Введите средний балл'}),
        }