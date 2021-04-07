from django.db import models
from django.urls import reverse

from .fields import IntegerRangeField


class Position(models.Model):
    positionID = models.AutoField(primary_key=True, verbose_name='ID')
    positionName = models.CharField(max_length=15, verbose_name='Должность')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return "{}".format(self.positionName)


class Person(models.Model):
    personID = models.AutoField(primary_key=True, verbose_name='ID')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    positionID = models.ForeignKey('Position', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)

    def get_absolute_url(self):
        return reverse('view_person', kwargs={'pk': self.personID})


class Student(models.Model):
    studentID = models.AutoField(primary_key=True, verbose_name='ID')
    personID = models.ForeignKey('Person', on_delete=models.PROTECT)
    classID = models.ForeignKey('Class', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return "{} {} {}".format(Person.surname, Person.name, Person.patronymic)

    def get_absolute_url(self):
        return reverse('view_student', kwargs={'pk': self.studentID})


class Class(models.Model):
    classID = models.AutoField(primary_key=True, verbose_name='ID')
    className = models.CharField(max_length=5, verbose_name='Наименование класса')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return self.className


class Discipline(models.Model):
    disciplineID = models.AutoField(primary_key=True, verbose_name='ID')
    nameDiscipline = models.CharField(max_length=30, verbose_name='Название дисциплины')


class Curriculum(models.Model):
    curriculumID = models.AutoField(primary_key=True, verbose_name='ID')
    personID = models.ForeignKey('Person', on_delete=models.PROTECT)
    classID = models.ForeignKey('Class', on_delete=models.PROTECT)
    disciplineID = models.ForeignKey('Discipline', on_delete=models.PROTECT)


class Task(models.Model):
    taskID = models.AutoField(primary_key=True, verbose_name='ID')
    taskName = models.CharField(max_length=50, verbose_name='Название задания')
    comments = models.TextField(verbose_name='Комментарии к заданию')
    startDateTime = models.DateTimeField(verbose_name='Дата и вермя начала')
    endDateTime = models.DateTimeField(verbose_name='Дата и время окончания')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.taskName


class Mark(models.Model):
    markID = models.AutoField(primary_key=True, verbose_name='ID')
    score = IntegerRangeField(min_value=0, max_value=100)
    studentID = models.ForeignKey('Student', on_delete=models.PROTECT)
    taskID = models.ForeignKey('Task', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return self.score
