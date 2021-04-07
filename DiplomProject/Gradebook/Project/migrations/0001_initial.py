# Generated by Django 3.1.7 on 2021-04-05 13:06

import Project.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('classID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(max_length=5, verbose_name='Наименование класса')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('disciplineID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nameDiscipline', models.CharField(max_length=30, verbose_name='Название дисциплины')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('personID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('positionID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('positionName', models.CharField(max_length=15, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=50, verbose_name='Название задания')),
                ('comments', models.TextField(verbose_name='Комментарии к заданию')),
                ('startDateTime', models.DateTimeField(verbose_name='Дата и вермя начала')),
                ('endDateTime', models.DateTimeField(verbose_name='Дата и время окончания')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('classID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Project.class')),
                ('personID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Project.person')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='positionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Project.position'),
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('markID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('score', Project.fields.IntegerRangeField()),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Project.student')),
                ('taskID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Project.task')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('curriculumID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('classID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Project.class')),
                ('disciplineID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Project.discipline')),
                ('personID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Project.person')),
            ],
        ),
    ]