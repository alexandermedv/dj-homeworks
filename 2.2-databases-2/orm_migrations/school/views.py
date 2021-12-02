from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = list(Student.objects.values())
    print(students)
    students = Student.objects.all()
    for student in students:
        print(student)
        for teacher in student.teachers.all():
            print('teacher:', teacher)
    # for teacher in Student.teachers.all():
    #     print(teacher)
    #     print(teacher.students.all())
    context = {'object_list': students}
    # context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
