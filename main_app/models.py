from django.db import models

class University(models.Model):
    full_name = models.CharField(max_length=255)  # Полное название университета
    short_name = models.CharField(max_length=50)  # Сокращенное название
    established_date = models.DateField()         # Дата создания

    def __str__(self):
        return self.short_name  # Отображение объекта в виде строки

class Student(models.Model):
    full_name = models.CharField(max_length=255)  # ФИО студента
    birth_date = models.DateField()               # Дата рождения
    university = models.ForeignKey(University, on_delete=models.CASCADE)  # Связь с университетом
    enrollment_year = models.PositiveIntegerField()  # Год поступления

    def __str__(self):
        return self.full_name  # Отображение объекта в виде строки