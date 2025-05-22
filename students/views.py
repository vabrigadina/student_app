from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.db.models import Avg, Count

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def student_list(request):
    sort_by = request.GET.get('sort_by', 'full_name')
    filter_specialization = request.GET.get('specialization', '')
    filter_course = request.GET.get('course', '')

    students = Student.objects.all()
    if filter_specialization:
        students = students.filter(specialization=filter_specialization)
    if filter_course:
        students = students.filter(course=filter_course)

    students = students.order_by(sort_by)

    stats = Student.objects.aggregate(
        avg_grade=Avg('average_grade'),
        total_students=Count('id')
    )

    # Получаем статистику по специализациям
    specialization_stats_raw = Student.objects.values('specialization').annotate(count=Count('id'))
    # Преобразуем ключи специализаций в читаемые названия
    specialization_stats = []
    for stat in specialization_stats_raw:
        readable_name = dict(Student.SPECIALIZATION_CHOICES).get(stat['specialization'], stat['specialization'])
        specialization_stats.append({
            'specialization': readable_name,
            'count': stat['count']
        })

    return render(request, 'students/student_list.html', {
        'students': students,
        'stats': stats,
        'specialization_stats': specialization_stats,
        'specialization_choices': Student.SPECIALIZATION_CHOICES,
        'course_choices': [(i, str(i)) for i in range(1, 5)],
        'current_specialization': filter_specialization,
        'current_course': filter_course,
        'current_sort': sort_by,
    })