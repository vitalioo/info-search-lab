from django.shortcuts import render, get_object_or_404, redirect
from .models import University, Student
from .forms import UniversityForm, StudentForm

# Университеты

def university_list(request):
    universities = University.objects.all()  # Получаем список всех университетов
    return render(request, 'university/university_list.html', {'universities': universities})

def university_create(request):
    form = UniversityForm(request.POST or None)
    if form.is_valid():
        form.save()  # Сохраняем новую запись
        return redirect('university_list')
    return render(request, 'university/university_form.html', {'form': form})

def university_update(request, pk):
    university = get_object_or_404(University, pk=pk)
    form = UniversityForm(request.POST or None, instance=university)
    if form.is_valid():
        form.save()  # Обновляем запись
        return redirect('university_list')
    return render(request, 'university/university_form.html', {'form': form})

def university_delete(request, pk):
    university = get_object_or_404(University, pk=pk)
    if request.method == 'POST':
        university.delete()  # Удаляем запись
        return redirect('university_list')
    return render(request, 'university/university_confirm_delete.html', {'object': university})

# Студенты

def student_list(request):
    students = Student.objects.all()  # Получаем список всех студентов
    return render(request, 'student/student_list.html', {'students': students})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()  # Сохраняем новую запись
        return redirect('student_list')
    return render(request, 'student/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()  # Обновляем запись
        return redirect('student_list')
    return render(request, 'student/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()  # Удаляем запись
        return redirect('student_list')
    return render(request, 'student/student_confirm_delete.html', {'object': student})