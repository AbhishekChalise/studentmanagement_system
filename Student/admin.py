from django.contrib import admin

from .models import Student_model
# Register your models here.
from .models import Grade

admin.site.register(Student_model)
admin.site.register(Grade)

