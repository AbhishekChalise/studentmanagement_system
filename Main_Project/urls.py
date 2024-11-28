"""
URL configuration for Main_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from User.views import login_admin,log_out
from Student.views import register
from django.conf import settings
from django.conf.urls.static import static 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Student.views import show_students
from teacher.views import show_teacher,edit_teacher,delete_teacher
from Student.views import edit_students,delete_student
from Student.views import home
from courses.views import course_list,add_course,teacher_list,teacher_addcourse
from teacher.views import edit_teacher,show_teacher,delete_teacher
from Student.views import Assign_Grade,Show_grade,Course_grades
from User.views import ChangePasswordView

urlpatterns = [
    path('',home,name = 'home'),
    path('admin/', admin.site.urls),
    path('login/', login_admin, name='login'),
    path('register/', register, name='student_registration'),
    path('logout/', log_out, name='logout'),
    path('show/',show_students,name = 'show'),
    path('show_teacher/',show_teacher , name = 'ShowTeacher'),
    path('student/edit/<int:id>/',edit_students,name='edit_student'),
   #path('teacher/edit/<int:id>/',edit_teacher,name='edit_teacher'),
    path('student/delete/<int:id>/' ,delete_student,name = 'delete_student'),
    path('teacher/edit/<int:id>/',edit_teacher,name = 'edit_teacher'),
    path('teacher/delete/<int:id>/',delete_teacher , name = 'delete_teacher'),
    path('course_list/<int:id>/',course_list,name= 'course_list'),
    path('add_course/<int:id>/',add_course,name = 'add_course'),
    path('teacher_list/<int:id>/',teacher_list,name ='teacher_courses'),
    path('teacher_addcourse/<int:id>/',teacher_addcourse,name = 'teacher_add_course'),
    path('assign_grade/<int:student_models_id>/<int:course_models_id>/',Assign_Grade,name = 'Assign_grade'),
    path('show_grade/<int:student_models_id>/<int:course_models_id>',Show_grade, name = 'Show_grade'),
    path('course_grades/<int:student_models_id>',Course_grades , name = 'Course_grades')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]
