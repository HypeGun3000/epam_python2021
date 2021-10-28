import csv

from django.core.management.base import BaseCommand
from main.models import HomeworkResult


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.csv', 'w') as file:
            for i in self.get_objects():
                print(i.last_name_student)
                csv_writer = csv.writer(file, delimiter=',')
                csv_writer.writerow([i.last_name_student,
                                     i.data_created,
                                     i.last_name_teacher])
        return f'Done'

    def get_objects(self):
        return HomeworkResult.objects.all()
