from django.db import models

# Create your models here.
class student_details(models.Model):
    # Profile_Photo=models.ImageField(upload_to='Images/school_app_files/student_photos/')
    Name=models.CharField(max_length=50)
    Roll_Number=models.CharField(max_length=10,unique=True)
    Class=models.PositiveIntegerField()
    Section=models.CharField(max_length=1)
    Gender=models.CharField(max_length=50)
    Date_of_Birth=models.DateField()
    Email=models.EmailField(unique=True)
    Student_ph_No=models.PositiveBigIntegerField(unique=True)
    fee=models.FloatField(default=30000)
    Admission_Date=models.DateField(auto_now_add=True)

class teachers_details(models.Model):
    # Profile_Photo=models.ImageField(upload_to='Images/school_app_files/teachers_photos/')
    Employee_ID=models.CharField(max_length=50,unique=True)
    Full_Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Date_of_Birth=models.DateField()
    Qualification=models.CharField(max_length=50)
    Subject=models.CharField(max_length=50)
    Experience_Years=models.FloatField()
    Joining_Date=models.DateField(auto_now_add=True)
    Salary=models.FloatField(default=40000)
    Contact_Number=models.PositiveBigIntegerField(unique=True)
    Email=models.EmailField(unique=True)