from django import forms
from school_app import models


class student_form(forms.ModelForm):
    class Meta:
        model = models.student_details
        fields = "__all__"
        exclude = ['Admission_Date']  # auto-filled
        
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Enter student full name'}),
            'Roll_Number': forms.TextInput(attrs={'placeholder': 'Enter unique roll number'}),
            'Class': forms.NumberInput(attrs={'placeholder': 'Enter class (1–12)'}),
            'Section': forms.TextInput(attrs={'placeholder': 'Enter section (A/B/C...)'}),
            'Gender': forms.TextInput(attrs={'placeholder': 'Enter gender'}),
            'Date_of_Birth': forms.DateInput(attrs={'type': 'date'}),
            'Email': forms.EmailInput(attrs={'placeholder': 'Enter student email'}),
            'Student_ph_No': forms.NumberInput(attrs={'placeholder': 'Enter phone number'}),
            'fee': forms.NumberInput(attrs={'placeholder': 'Enter fee amount'}),
        }


class teachers_form(forms.ModelForm):
    class Meta:
        model = models.teachers_details
        fields = "__all__"
        exclude = ['Joining_Date']  # auto-filled

        widgets = {
            'Employee_ID': forms.TextInput(attrs={'placeholder': 'Enter employee ID'}),
            'Full_Name': forms.TextInput(attrs={'placeholder': 'Enter teacher full name'}),
            'Gender': forms.TextInput(attrs={'placeholder': 'Enter gender'}),
            'Date_of_Birth': forms.DateInput(attrs={'type': 'date'}),
            'Qualification': forms.TextInput(attrs={'placeholder': 'Enter qualification'}),
            'Subject': forms.TextInput(attrs={'placeholder': 'Enter subject'}),
            'Experience_Years': forms.NumberInput(attrs={'placeholder': 'Years of experience'}),
            'Salary': forms.NumberInput(attrs={'placeholder': 'Enter salary'}),
            'Contact_Number': forms.NumberInput(attrs={'placeholder': 'Enter contact number'}),
            'Email': forms.EmailInput(attrs={'placeholder': 'Enter teacher email'}),
        }










# from django import forms
# from school_app import models
# # Create your forms here.
# class student_form(forms.ModelForm):
#     class Meta:
#         model=models.student_details
#         fields="__all__"
# class teachers_form(forms.ModelForm):
#     class Meta:
#         model=models.teachers_details
#         fields="__all__"