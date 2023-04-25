from django.shortcuts import render, redirect
from .form import StudentForm
from .models import Student


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    context = {'form': form}
    return render(request, 'add_student.html', context)



def student_list(request):
    students = Student.objects.all()
    for student in students:
        student.total_marks = student.physics_marks + student.chemistry_marks + student.maths_marks + student.cs_marks
        student.percentage = round(student.total_marks / 4, 2)

    context = {'students': students}
    return render(request, 'student_list.html', context)