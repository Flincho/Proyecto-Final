from django.contrib import admin

from app_1.models import Course, Student, Profesor, Homework

admin.site.register(Course)

admin.site.register(Student)

admin.site.register(Profesor)

admin.site.register(Homework)
