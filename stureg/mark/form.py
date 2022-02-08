from django import forms
from mark.models import StudentMark

class StudentMarkForm(forms.ModelForm):
    class Meta:

        model = StudentMark
        fields = '__all__'