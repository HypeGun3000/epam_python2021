from django.contrib import admin
from .models import Human, Homework, Student, HomeworkResult, Teacher


admin.site.register(Human)
admin.site.register(Homework)
admin.site.register(Student)
admin.site.register(HomeworkResult)
admin.site.register(Teacher)

