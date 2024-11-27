from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from courses.models import Course_models
from courses.forms import Course_forms
from Student.models import Student_model
from teacher.models import Teacher_models
# def login_admin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username)
#         print('password')

#         # Authenticate user
#         user = authenticate(request, username=username, password=password)

#         # Check if user is None (authentication failed)
#         if user is None:
#             print("Authentication failed")
#             # You can add a message here to notify the user (e.g., invalid username/password)
#             return render(request, 'Login.html', {'error': 'Invalid credentials'})
#         # Check if the user is a superuser
#         if user.is_superuser:
#             print("Hey SuperUser")
#         if user.is_student:
#             print('He is a student!!!')
#             print(user.course.Course_name)
#         if user.is_teacher:
#             print('He is a teacher!!!')

#         print(user)
#         # Log in the user
#         login(request, user)

#         print(f'{username} successfully logged in')
#         # Redirect to the admin page or wherever you want after login
#         if user.is_superuser:
#             return redirect('student_registration')
#         elif user.is_student:
#             context = {
#                 'user':user
#             }
#             return render(request ,'Student.html',context)
#         elif user.is_teacher:
#             context = {
#                 'user':user
#             }
#             return redirect(request,'Teacher.html',context)
#     else:
#         return render(request, 'Login.html')
def log_out(request):
    logout(request)
    return redirect('login')
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# def login_admin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username)
#         print('password')

#         # Authenticate user
#         user = authenticate(request, username=username, password=password)

#         # Check if user is None (authentication failed)
#         if user is None:
#             print("Authentication failed")
#             # You can add a message here to notify the user (e.g., invalid username/password)
#             return render(request, 'Login.html', {'error': 'Invalid credentials'})

#         # Check if the user is a superuser
#         if user.is_superuser:
#             print("Hey SuperUser")
#         print(user)
#         # Log in the user
#         login(request, user)
#         if user.is_student:
#             print('He is a student!!!')
#             courses = user.course.all()  # Get all the courses associated with the student
#             print(courses)
#             if courses.exists():
#                 for course in courses:
#                     print(course.Course_name)  # Print each course name
#             else:
#                 print('Man the course doesnot exists!!!!')
#         if user.is_teacher:
#             print('He is a teacher!!!')
#         print(f'{username} successfully logged in')
#         # Redirect to the appropriate page based on the user type
#     else:
#         return render(request, 'Login.html')

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from Student.models import Student_model
# from courses.models import Course_models

def login_admin(request):
    if request.method == 'POST':
        # Get username and password from the request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username = username, password = password)

        if user is None:  # Authentication failed
            return render(request, 'Login.html', {'error': 'Invalid credentials'})
        # Log in the user
        login(request, user)
        print('User Successfully logged in!!! ')
        # Handle superuser login
        if user.is_superuser:
            return redirect('student_registration')

        # Handle student login
        elif user.is_student:
            try:
                # Access the associated Student_model instance
                student = Student_model.objects.get(user=user)  # Assuming there's a 'user' field
                print(student)
                # Retrieve all courses associated with the student
                courses = student.course.all()  # Assuming 'course' is a related field in Student_model
                
                context = {
                    'user': user,
                    'courses': courses,  # Now courses is defined
                }
                return render(request, 'Student.html', context)

            except Student_model.DoesNotExist:
                # Handle case where a Student_model does not exist
                return render(request, 'Login.html', {'error': 'Student profile not found.'})

        # Handle teacher login
        elif user.is_teacher:
            try:
                teacher = Teacher_models.objects.get(user=user)
                print(teacher)
                course = teacher.course.all()
                
                context = {
                'user': user,
                'course':course,
                 }
                return render(request, 'teacher.html', context)
            except Teacher_models.DoesNotExist:
                # Handle case when teacher does not exists!!!!
                return render(request ,'Login.html',{'error':'Teacher doesnot exists!!!!!'} )

        # Fallback if user role is not recognized
        else:
            logout(request)  # Log out user if role is not defined
            return render(request, 'Login.html', {'error': 'User role not recognized.'})

    # If request is GET, render the login page
    return render(request, 'Login.html')
