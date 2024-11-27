from django.shortcuts import render
from teacher.models import Teacher_models
from Student.views import register
from django.shortcuts import get_object_or_404
from teacher.forms import Teacher_forms
from django.shortcuts import redirect

# Create your views here.

#def register_teacher(request):
#    if request.method == 'GET':
#        form  = 

def show_teacher(request):
    teacher_obj = Teacher_models.objects.all()
    teacher_session = request.session.get('student')
    context = {
        'teacher_obj' : teacher_obj,
        'teacher_session':teacher_session
    }
    return render(request , 'show_teacher.html',context)

def edit_teacher(request , id):
    teacher_obj = Teacher_models.objects.filter(id = id).last

    get_instance = get_object_or_404(Teacher_models , id=id)

    if request.method == 'GET':
        # Render the edit method
        form = Teacher_forms(instance = get_instance)
        context = {
            'form':form,
            'teacher':get_instance
        }
        return render(request , 'edit.html' , context)
    
    elif request.method == 'POST':
        form = Teacher_forms(request.POST , instance= get_instance)
        if form.is_valid():
            form.save()
            return redirect('edit_students')
        
        else:
            context = {
                'form' : form , 
                'teacher' : get_instance,
                'error': 'please correct the code'
            }
            return render('ShowTeacher')
        
def delete_teacher(request,id):
    teacher  = Teacher_models.objects.get(id = id)
    teacher.Tdeleted = True
    teacher.save()
    return redirect('show')

        


    






