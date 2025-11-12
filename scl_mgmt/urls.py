"""
URL configuration for scl_mgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from school_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_fun, name='landing_page'),
    path('register_page/', views.register_fun, name='registration_page'),
    path('login_page/', views.login_fun, name='login_page'),

    path('home', views.main_fun, name='home'), 
    path('student_data_display/', views.student_form_fun, name='student_table'),
    path('student_updation/<int:id>/', views.student_update_fun, name='student_update'),
    path('student_deletion/<int:id>/', views.student_delete_fun, name='student_delete'),

    path('teacher_data_display/', views.teachers_form_fun, name='teach_table'),
    path('teacher_updation/<int:id>/', views.teacher_update_fun, name='teach_update'),
    path('teacher_deletion/<int:id>/', views.teacher_delete_fun, name='teach_delete'),
]