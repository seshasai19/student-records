from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'student_class', 'roll_no', 'marks']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. John Doe', 'required': True}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 20', 'min': 1, 'max': 120, 'required': True}),
            'student_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 10th Grade / CS-A', 'required': True}),
            'roll_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 101', 'min': 1, 'required': True}),
            'marks': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 85', 'min': 0, 'max': 100, 'required': True}),
        }

    def clean_roll_no(self):
        roll_no = self.cleaned_data.get('roll_no')
        instance = self.instance
        if Student.objects.filter(roll_no=roll_no).exclude(pk=instance.pk if instance else None).exists():
            raise forms.ValidationError("A student with this Roll Number already exists.")
        return roll_no
