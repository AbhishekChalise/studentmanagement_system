from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from Student.models import Student_model
from Student.forms import Student_Forms
from courses.models import Course_models
from courses.forms import Course_forms
from django.http import HttpResponse
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
    student = Student_model.objects.filter(id=id).first()
    if not student:
        return HttpResponse("Student not found", status=404)
    course = student.course.all()
    if request.method == 'POST':
        form = Course_forms(request.POST)
        current_course_data = form.cleaned_data('Course_name')
        if current_course_data in course:
            print('The Course doesnot exists!!!!')

        if form.is_valid():
            course = form.save()
            student.course.add(course)  # Link course to student

            return redirect('course_list', id=id)  # Redirect to the course list page

    form = Course_forms()
    return render(request, 'add_course.html', {'form': form, 'id': id})








    