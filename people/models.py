from django.db import models

# Create your models here.
class Branch(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес филиала')
    short_name = models.CharField(max_length=50, verbose_name='Короткое название')

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название отдела')
    floor = models.IntegerField(verbose_name='Этаж')
    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='departments',
        verbose_name='Филиал'
    )

class Employee(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    position = models.CharField(max_length=100, verbose_name='Должность')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees',
        verbose_name='Отдел'
    )