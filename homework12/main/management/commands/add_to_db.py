from django.core.management.base import BaseCommand

from main.models import Homework, HomeworkResult, Human, Student, Teacher


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.human_add()
        self.homework_add()
        self.student_add()
        self.homeworkresult_add()
        self.teacher_add()

    def human_add(self):
        human = Human(
            name='Ivan',
            surname='Ivanon',
            comment='Administrator'
        )
        human.save()
        return human

    def homework_add(self):
        homework = Homework(
            text='Create 3D model',
            deadline=3,
            comment='Use models from lesson 3'
        )
        homework.save()
        return homework

    def student_add(self):
        student = Student(
            first_name_student='German',
            last_name_student='Classico',
            comment='Middle grade 4.2'
        )
        student.save()
        return student

    def homeworkresult_add(self):
        homeworkresult = HomeworkResult(
            text='Create 3D model',
            last_name_student='Classico',
            solution='3D model ...',
            comment='Have some questions...'
        )
        homeworkresult.save()
        return homeworkresult

    def teacher_add(self):
        teacher = Teacher(
            first_name_teacher='Mariya',
            last_name_teacher='Prohorova',
            comment='Teacher of Programming'
        )
        teacher.save()
        return teacher
