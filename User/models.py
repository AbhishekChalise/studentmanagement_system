from django.db import models
from django.contrib.auth.models import AbstractUser
from courses.models import Course_models
class User_Model(AbstractUser):
    SCIENCE = 'Science'
    MATHS = 'Maths'
    C_PROGRAMMING = 'C Programming'
    COMPUTER_SCIENCE = 'Computer Science'

    COURSE_CHOICES = [
        (SCIENCE, 'Science'),
        (MATHS, 'Maths'),
        (C_PROGRAMMING, 'C Programming'),
        (COMPUTER_SCIENCE, 'Computer Science'),
    ]
    course = models.ManyToManyField(Course_models , related_name = 'User_Course_FK',null = True , blank = True)
    course1 = models.CharField(max_length=255,null=True,blank = True , choices = COURSE_CHOICES )
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null = True,)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='custom_user_groups',
    #     blank=True
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='custom_user_permissions',
    #     blank=True
    # )

    class Meta:
        db_table = 'user'
