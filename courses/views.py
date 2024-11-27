from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from Student.forms import Student_Forms
from courses.models import Course_models
from courses.forms import Course_forms
from django.http import HttpResponse
from teacher.models import Teacher_models
from teacher.forms import Teacher_forms
from Student.models import Student_model
# Create your views here.

# def Assign_course(request , id):
#     course_student = get_object_or_404(Student_model , id = id)

#     if request.method == 'POST':
#         form = Student_Forms(request.POST , instance = course_student)
#         if form.is_valid:
#             form.save()
#             return redirect('')
#         else:
#             form = Student_Forms(instance = course_student)
#             context = {
#                 'form':form,
#                 'course_student':course_student
#             }
#             return render(request , '.html',context)


# def register_course(request):
def course_list(request, id):
    student = Student_model.objects.filter(id=id).last()
    
    if not student:
        return HttpResponse("Student not found", status=404)
    
    courses = student.course.all()  # Correct field name
    print('This is your course:', courses)

    context = {
        'courses': courses,
        'id': id
    }
    return render(request, 'course_list.html', context)

def add_course(request, id):
    existing_course = None
    student = Student_model.objects.filter(id=id).first()
    if not student:
        return HttpResponse("Student not found", status=404)
    course = student.course.all()
    if request.method == 'POST':
        form = Course_forms(request.POST)
        if form.is_valid():
            current_course_data = form.cleaned_data.get('Course_name')
            existing_course = student.course.filter(Course_name = current_course_data).first()
        if existing_course:
            print('The Course already exists!!!!')
        else:
            course = form.save()
            student.course.add(course)  # Link course to student
            return redirect('course_list', id=id)  # Redirect to the course list page

    form = Course_forms()
    return render(request, 'add_course.html', {'form': form, 'id': id})


def teacher_list(request , id):
    print(id)
    teacher = Teacher_models.objects.filter(id=id).last()
    print(teacher)
    if not teacher:
        return HttpResponse("Teacher Not Found",status = 404)
    teacher_courses = teacher.course.all()
    print('This is the teacher_course',teacher_courses)
    context = {
        'teacher_course':teacher_courses,
        'id':id
    }
    return render(request , 'teacher_list.html',context)

def teacher_addcourse(request,id):
    teacher = Teacher_models.objects.filter(id = id).last()
    if not teacher:
        print('Teacher not found',status = 404)
    course = teacher.course.all()

    if request.method == 'POST':
        form = Course_forms(request.POST)
        if form.is_valid():
            current_course_data = form.cleaned_data.get('Course_name')
            existing_course = teacher.course.filter(Course_name = current_course_data).first()
            if existing_course:
                print('The Course already exists!!!')
            else:
                course = form.save()
                teacher.course.add(course)
                return redirect('teacher_courses',id=id)
    form = Course_forms()
    return render(request , 'teacher_add_course.html',{'form':form , 'id':id})
        



    # def add_course(request, id):
    # student = Student_model.objects.filter(id=id).first()
    # if not student:
    #     return HttpResponse("Student not found", status=404)
    # course = student.course.all()
    # if request.method == 'POST':
    #     form = Course_forms(request.POST)
    #     if form.is_valid():
    #         current_course_data = form.cleaned_data.get('Course_name')
    #     if current_course_data in course:
    #         print('The Course already exists!!!!')
    #     else:
    #         course = form.save()
    #         student.course.add(course)  # Link course to student

    #         return redirect('course_list', id=id)  # Redirect to the course list page

    # form = Course_forms()
    # return render(request, 'add_course.html', {'form': form, 'id': id})  is this correct??







    