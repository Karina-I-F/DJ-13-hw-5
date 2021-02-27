from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    list_students = []
    students = Student.objects.all().prefetch_related('teachers').order_by('group')
    for student in students:
        object_student = {}
        object_student['name'] = student.name
        object_student['group'] = student.group
        object_student['teachers'] = student.teachers.all().order_by('name').values('name', 'subject')

        list_students.append(object_student)
    context = {'list_students': list_students}

    return render(request, template, context)
