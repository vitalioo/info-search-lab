from django.contrib import admin
from .models import University, Student

admin.site.register(University)  # Регистрируем модель University
admin.site.register(Student)     # Регистрируем модель Student