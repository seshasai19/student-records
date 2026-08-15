from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Student
from .forms import StudentForm
from .serializers import StudentSerializer


def student_list(request):
    students = Student.objects.all().order_by('-id')

    # Get filters from GET request
    search_name = request.GET.get('search_name', '').strip()
    search_age = request.GET.get('search_age', '').strip()
    search_class = request.GET.get('search_class', '').strip()
    search_roll_no = request.GET.get('search_roll_no', '').strip()
    search_marks = request.GET.get('search_marks', '').strip()

    if search_name:
        students = students.filter(name__icontains=search_name)
    if search_class:
        students = students.filter(student_class__icontains=search_class)
    if search_age:
        if search_age.isdigit():
            students = students.filter(age=int(search_age))
        else:
            students = students.none()
    if search_roll_no:
        if search_roll_no.isdigit():
            students = students.filter(roll_no=int(search_roll_no))
        else:
            students = students.none()
    if search_marks:
        if search_marks.isdigit():
            students = students.filter(marks=int(search_marks))
        else:
            students = students.none()

    context = {
        'students': students,
        'search_name': search_name,
        'search_age': search_age,
        'search_class': search_class,
        'search_roll_no': search_roll_no,
        'search_marks': search_marks,
    }
    return render(request, 'student_list.html', context)


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form, 'title': 'Add New Student'})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_edit.html', {'form': form, 'student': student})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})


# REST Framework ViewSet for API
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['student_class', 'age', 'roll_no']
    search_fields = ['name', 'student_class']
    ordering_fields = ['id', 'name', 'marks', 'roll_no', 'age']
