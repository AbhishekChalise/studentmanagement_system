from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Student_Forms
from Student.models import Student_model
from User.forms import User_Form
from django.contrib.auth import authenticate, login
from User.models import User_Model
from django.shortcuts import get_object_or_404

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

    if request.method == 'GET':
        form = Student_Forms(instance = get_instance)
        context = {
            'form': form,
            'student': get_instance 
        }
        return render(request , 'edit.html',context)
    
    elif request.method == 'POST':
        form = Student_Forms(request.POST , instance = get_instance)
        if form.is_valid():
            form.save()
            # save the form
            return redirect()
        
        else:
            context = {
                'form':form,
                'student':get_instance,
                'error' : 'Please Correct The Error below'
            }
            return render(request , 'Teacher_edit.html',context)
        
def delete_student(request,id):
    student = Student_model.objects.get(id = id)
    student.sdelete = True
    student.save()
    return redirect('show')


login_required(login_url = '/home/')
def home(request):
    return render(request , 'index.html')







