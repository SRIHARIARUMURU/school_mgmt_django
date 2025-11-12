from django.shortcuts import render, redirect
from school_app import forms, models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def landing_fun(request):
    return render(request, 'school_app_html_files/home.html')

# Home Page
def main_fun(request):
    return render(request, 'school_app_html_files/index.html')

# ------------------- REGISTER LOGIN -------------------
def register_fun(request):
    msg=''
    if request.method=='POST':
        user_name=request.POST.get('username')
        user_email=request.POST.get('email')
        pwd=request.POST.get('password')
        confirm_pwd=request.POST.get('Confirm_password')
        if pwd!=confirm_pwd:
            msg='Enter Correct Password'
        elif User.objects.filter(email=user_email).exists():
            msg='User already exists'
        else:
            user=User.objects.create_user(username=user_name,email=user_email,password=pwd)
            user.save()
            return redirect('login_page')
    return render(request,'school_app_html_files/register_page.html', {'msg':msg})
        
        

def login_fun(request):
    msg=''
    if request.method=='POST':
        user_name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(username=user_name, password=pwd )
        if user is not None:
            login(request,user)
            msg='login success'
            return redirect('home')
        else:
            msg='invalid credintials'
    return render(request, 'school_app_html_files/login_page.html' ,{'msg':msg})


# ------------------- STUDENTS -------------------
def student_form_fun(request):
    if request.method == 'POST':
        stu_form = forms.student_form(request.POST)
        if stu_form.is_valid():
            stu_form.save()
            return redirect('student_table') 
    else:
        stu_form = forms.student_form()
    stu_table = models.student_details.objects.all()
    return render(request, 'school_app_html_files/students.html', {
        'stu_form': stu_form,
        'stu_table': stu_table
    })


def student_update_fun(request, id):
    stu_table = models.student_details.objects.get(id=id)
    if request.method == 'POST':
        stu_form = forms.student_form(request.POST, instance=stu_table)
        if stu_form.is_valid():
            stu_form.save()
            return redirect('student_table')
    else:
        stu_form = forms.student_form(instance=stu_table)
    return render(request, 'school_app_html_files/students_update.html', {
        'stu_form': stu_form
    })


def student_delete_fun(request, id):
    student = models.student_details.objects.get(id=id)
    student.delete()
    return redirect('student_table')


# ------------------- TEACHERS -------------------
def teachers_form_fun(request):
    if request.method == 'POST':
        teach_form = forms.teachers_form(request.POST)
        if teach_form.is_valid():
            teach_form.save()
            return redirect('teach_table')
    else:
        teach_form = forms.teachers_form()

    teach_table = models.teachers_details.objects.all()
    return render(request, 'school_app_html_files/teachers.html', {
        'teach_form': teach_form,
        'teach_table': teach_table
    })


def teacher_update_fun(request, id):
    teacher = models.teachers_details.objects.get(id=id)
    if request.method == 'POST':
        teach_form = forms.teachers_form(request.POST, instance=teacher)
        if teach_form.is_valid():
            teach_form.save()
            return redirect('teach_table')
    else:
        teach_form = forms.teachers_form(instance=teacher)
    return render(request, 'school_app_html_files/teachers_update.html', {
        'teach_form': teach_form
    })


def teacher_delete_fun(request, id):
    teacher = models.teachers_details.objects.get(id=id)
    teacher.delete()
    return redirect('teach_table')


    return render(request, 'school_app_html_files/index.html')
# 
