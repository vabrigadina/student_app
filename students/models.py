from django.db import models

class Student(models.Model):
    SPECIALIZATION_CHOICES = [
        ('intercultural', 'Межкультурная коммуникация'),
        ('teaching', 'Преподавание'),
        ('translation', 'Перевод'),
    ]

    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    program = models.CharField(max_length=100, verbose_name="Образовательная программа")
    course = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)], verbose_name="Курс")
    group_number = models.CharField(max_length=10, verbose_name="Номер группы")
    specialization = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES, verbose_name="Специализация")
    graduation_year = models.IntegerField(verbose_name="Год окончания обучения")
    average_grade = models.FloatField(verbose_name="Средний балл")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"