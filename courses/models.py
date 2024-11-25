from django.db import models

# Create your models here.
# Pre defined Course Choices

COURSE_CHOICES = [
    ('ComputerScience','ComputerScience'),
    ('Mathematics','Mathematics'),
    ('Physics','Physics'),
    ('Chemistry','Chemistry'),
    ('Biology','Biology'),
]

class Course_models(models.Model):
    Course_name = models.CharField(max_length=100 , choices= COURSE_CHOICES )
    description = models.TextField(blank = True , null = True)

    class Meta:
        db_table = 'course'

