from django import forms
from school_app import models
# Create your forms here.
class student_form(forms.ModelForm):
    class Meta:
        model=models.student_details
        fields="__all__"
class teachers_form(forms.ModelForm):
    class Meta:
        model=models.teachers_details
        fields="__all__"