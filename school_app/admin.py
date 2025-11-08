from django.contrib import admin
from school_app import models
# Register your models here.
class student_admin(admin.ModelAdmin):
    list_display=['Name','Roll_Number','Class','Section','Gender','Date_of_Birth','Email','Student_ph_No','fee','Admission_Date']
    list_filter=['Roll_Number','Class','Section','Gender']
    search_fields=['Roll_Number','Name']
    ordering=['Class']
admin.site.register(models.student_details,student_admin)

class teachers_admin(admin.ModelAdmin):
    list_display=['Employee_ID','Full_Name','Gender','Date_of_Birth','Qualification','Subject','Experience_Years','Joining_Date','Salary','Contact_Number','Email']
    list_filter=['Gender', 'Subject','Joining_Date', 'Experience_Years' ]
    search_fields=['Employee_ID','Full_Name']
    ordering=['Employee_ID']
admin.site.register(models.teachers_details,teachers_admin)
