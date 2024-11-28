from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Student_Forms
from Student.models import Student_model
from User.forms import User_Form
from django.contrib.auth import authenticate, login
from User.models import User_Model
from django.shortcuts import get_object_or_404
from courses.models import Course_models
from Student.models import Grade

def register(request):
    if request.method == 'POST':
        form = User_Form(request.POST,request.FILES)
        if form.is_valid():
            try:
                # Save the user instance

                print('successfully validated!!!')
                user_instance = form.save(commit=False)

                user_instance.is_student = 'is_student' in request.POST
                user_instance.is_teacher = 'is_teacher' in request.POST
                # print(user_instance.profile_picture)
                # Explicitly set `is_student` to True
                user_instance.save()
                # Create A Session:
                request.session.flush()
                request.session['student'] = {
                    'name':str(user_instance.username),
                    'course':str(user_instance.course),
                    'birth_date':str(user_instance.birth_date),
                    'is_student':str(user_instance.is_student),
                    'is_teacher':str(user_instance.is_teacher),
                }
                print(request.session['student'])
                print(request.session.items())
                # Log in or redirect after successful registration
                return redirect('show')

            except Exception as e:
                print(f'Error: {e}')
                return render(request, 'error.html', {'error': 'Could not register user.'})
        else:
           print(form.errors)  # Print form validation errors
           return render(request, 'Registration.html', {'form': form, 'error': form.errors})

    else:
        form = User_Form()
        return render(request, 'Registration.html', {'form': form})


def show_students(request):
    student_obj = Student_model.objects.filter(sdelete = False)
    student_session = request.session.get('student',{})
    student_name = student_session.get('name' , 'No name Found')
    print(student_name)
    context = {
        'student_obj':student_obj,
        'student_session' : student_session
    }
    return render(request , 'show.html',context)

def edit_students(request , id):
    student_obj = Student_model.objects.filter(id = id).last

    get_instance = get_object_or_404(Student_model , id = id)

    #birth_date = get_instance.user.birth_date

    if request.method == 'GET':
        form = Student_Forms(instance = get_instance)
        context = {
            'form': form,
            'student': get_instance,
          #  'birth_date':birth_date
        }
        return render(request , 'edit_student.html',context)
    
    elif request.method == 'POST':
        form = Student_Forms(request.POST , instance = get_instance)
        print(form.errors)
        if form.is_valid():
            form.save()
            print('The form is valid!!!!, i am inside the edit_student')
            print(form.errors)
            # save the form
            return redirect('show')
    
        else:
            context = {
                'form':form,
                'student':get_instance,
                'error' : 'Please Correct The Error below'
            }
            return render(request , 'edit_student.html',context)
        
def delete_student(request,id):
    student = Student_model.objects.get(id = id)
    student.sdelete = True
    student.save()
    return redirect('show')


login_required(login_url = '/home/')
def home(request):
    return render(request , 'index.html')


from .models import Grade
from .forms import AssignGradeForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json

def Assign_Grade(request , student_models_id , course_models_id):
    # Get student and course object from the perticular course:

    student = get_object_or_404(Student_model , id = student_models_id)
    course = get_object_or_404(Course_models, id = course_models_id)

    # Get request to get the data!!!!!!

    if request.method == 'GET':
        context = {
            'student':student,  
            'course':course,
            'student_models_id':student_models_id,
            'course_models_id':course_models_id
        }
        return render(request , 'assign_grade.html' , context)
    
    elif request.method == 'POST':
        try:        
            if not student.course.filter(id = course_models_id):
                print(student.course.filter(id = course_models_id))
                print("error the course doesnot exists for the student!!!1")
                return JsonResponse({'error': 'Student is not enrolled in the course'},status = 404)
            
            print(request.POST,"hehehe") # Query Set from request.POST
            data = json.dumps(request.POST) # unpack Query Set to Dictionary.
            
            #body_unicode = request.body.decode('utf-8')
            
            #data = json.loads(request.body)
            grade_value = json.loads(data)
            print(type(grade_value) , 'This is grade value!!')
            print(grade_value["grade"] , 'This is grade value!!')

            if not grade_value['grade']:
                return JsonResponse({'error':'There is no grade assigned!!!!'},status = 400)

            valid_grade = ['A','B','C','D','E','F']

            if grade_value['grade'] not in valid_grade:
                return JsonResponse({'error':'Its not a valid grade please enter the valid grade!!!!'})

            # get grades from the students:
            # grade_value = request.post.get('grade')

            grade , created = Grade.objects.update_or_create(
            student = student,
            course  = course,
            defaults = {'grade':grade_value['grade']}
            ) 

            return JsonResponse({
                'message':'Grade Successfully assigned',
                'grade': grade.grade,
                'created':created
            }, status = 201 if created else 200)
        except json.JSONDecodeError:
            return JsonResponse({'error':'Invalid Json Data!!1'},status = 400)
        
# This is to show the student grades.
def Show_grade(request , student_models_id , course_models_id):
    student = get_object_or_404(Student_model ,id =  student_models_id)
    course = get_object_or_404(Course_models,id = course_models_id)

    # enrolled_course = student.course.all()
    # print(enrolled_course.values()) 
    #print(student)
    id_set = {student_models_id , course_models_id}
    grade_value = Grade.objects.filter( id__in  = id_set) # this will look and match with all ids in id field!!!!
    print(grade_value)
    list_grade = list(grade_value.values('grade'))
    print(type(list_grade))
    print(list_grade[0]['grade'])
    grade = list_grade[0]['grade']
    #print(grade_value,"This is the grade:")
    #print(type(grade_value))
    #gr = grade_value.values('grade')    
    #print(gr)
    context = {
        'grade' : grade,
        'student':student,
    }
    return render(request , 'show_grade.html', context)

def Course_grades(request, student_models_id,):
    student = get_object_or_404(Student_model, id=student_models_id)
    #course = get_object_or_404(Course_models , id=student_models_id)
    enrolled_courses = student.course.all()
    grades = Grade.objects.filter(student=student)
    print(grades.values() , "Hey this is the course values!!!!")
    # Create a mapping of course to grade
    course_grades = []
    for course in enrolled_courses:
        grade = grades.filter(course=course).first()  # Get grade for the course, if exists
        course_grades.append({
            'course_name': course.Course_name,
            'grade': grade.grade if grade else "N/A"  # Show 'N/A' if no grade exists
        })

    context = {
        'course_grades': course_grades,
    }
    return render(request, 'show_enrolled.html', context)

print("Hello World!!!!")

