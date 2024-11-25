from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from User.models import User_Model
from courses.models import Course_models

class Teacher_models(models.Model):
    user = models.OneToOneField(User_Model , on_delete = models.CASCADE , related_name= 'teacher_models_FK')
    Teacher_name = models.CharField(max_length = 255)
    course = models.ManyToManyField(Course_models , related_name = 'course_models_FK' , null= True , blank = True)
    Tdeleted = models.BooleanField(default = False)
    class Meta:
        db_table = 'teacher'

# Signal to create a Student_model after a new User is created
@receiver(post_save , sender = User_Model)
def create_teacher(sender , instance , created , **kwargs):
    if created and instance.is_teacher:
        Teacher_models.objects.create(user = instance , Teacher_name = instance.username)
        print(f'Teacher Created for: {instance.username}')

# Create your models here.
