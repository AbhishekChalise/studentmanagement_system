from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from User.models import User_Model
from courses.models import Course_models

class Student_model(models.Model):
    user = models.OneToOneField(User_Model, on_delete = models.CASCADE, related_name='student')
    Student_name = models.CharField(max_length=255)
    course_of_studey = models.CharField(max_length=255 , blank = True ,null = True)
    sdelete = models.BooleanField(default=False)
    course = models.ManyToManyField(Course_models , related_name = 'Student_Courses_FK')
    class Meta:
        db_table = 'student'

# Signal to create a Student_model after a new User is created
@receiver(post_save, sender=User_Model)
def create_student(sender, instance, created, **kwargs):
    if created and instance.is_student:  # Ensure the user is a student
        Student_model.objects.create(user=instance, Student_name=instance.username)
        print(f'Student created for: {instance.username}')