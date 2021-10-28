from django.db import models


class Human(models.Model):
    name = models.CharField('First Human name', max_length=50, null=True)
    surname = models.CharField('Last Human name', max_length=50, null=True)
    comment = models.TextField('Comment your table add', null=True)

    def __str__(self):
        return self.surname


class Homework(models.Model):
    text = models.TextField('Text homework', null=True)
    deadline = models.IntegerField('Deadline homework', null=True)
    comment = models.TextField('Comment your table add', null=True)

    def __str__(self):
        return self.text


class Student(models.Model):
    first_name_student =\
        models.CharField('First Student name', max_length=50, null=True)
    last_name_student =\
        models.CharField('Last Student name', max_length=50, null=True)
    comment = models.TextField('Comment your table add', null=True)

    def __str__(self):
        return self.last_name_student


class HomeworkResult(models.Model):
    text = models.TextField('Text homework', null=True)
    last_name_student =\
        models.CharField('Last Student name', max_length=50, null=True)
    last_name_teacher =\
        models.CharField('Last Teacher name', max_length=50, null=True)
    solution = models.TextField("Homework solution", null=True)
    data_created = models.DateTimeField("Add datatime", null=True)
    comment = models.TextField('Comment your table add', null=True)

    def __str__(self):
        return self.text


class Teacher(models.Model):
    first_name_teacher =\
        models.CharField('First Teacher name', max_length=50, null=True)
    last_name_teacher =\
        models.CharField('Last Teacher name', max_length=50, null=True)
    comment = models.TextField('Comment your table add', null=True)

    def __str__(self):
        return self.last_name_teacher
