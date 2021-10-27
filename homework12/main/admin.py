from django.contrib import admin

from .models import Homework, HomeworkResult, Human, Student, Teacher

admin.site.register(Human)
admin.site.register(Homework)
admin.site.register(Student)
admin.site.register(HomeworkResult)
admin.site.register(Teacher)

