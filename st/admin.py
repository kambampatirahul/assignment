from django.contrib import admin
from .models import student, assignment
# Register your models here.

admin.site.register(student)
#admin.site.register(teacher)
admin.site.register(assignment)