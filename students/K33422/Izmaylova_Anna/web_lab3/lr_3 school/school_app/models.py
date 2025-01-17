from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# кабинет
class Room(models.Model):
    room = models.IntegerField()

# ученики
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=(('male','male'), ('female','female')))

# класс
class Groups(models.Model):
    name = models.CharField(max_length=5)

# в каком классе учатся ученики
class StudentsGroup(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id =  models.ForeignKey(Groups, on_delete=models.CASCADE, null=True)

# учитель
class Teacher(AbstractUser):
    patronymic = models.CharField(max_length=30) # отчество
    group_id = models.ForeignKey(StudentsGroup, on_delete=models.CASCADE, null=True, blank=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    REQUIRED_FIELDS = ["first_name", "last_name", "patronymic", "group_id", "room_id"]

# предмет
class Subject(models.Model):
    subject = models.CharField(max_length=30)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=(('basic','basic'), ('profile','profile')))

# оценка 
class Grades(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=(('1','1'), ('2','2'), ('3','3'),('4','4'), ('5','5')))
    quarter = models.CharField(max_length=1, choices=(('1','1'), ('2','2'), ('3','3'),('4','4')))

# расписание 
class Timetable(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_id = models.ForeignKey(StudentsGroup, on_delete=models.CASCADE, null=True)
    day_of_week = models.CharField(max_length=30, choices=(('1','1'), ('2','2'), ('3','3'),('4','4'), ('5','5'), ('6','6')), default='1')
    lesson = models.CharField(max_length=30, choices=(('1','1'), ('2','2'), ('3','3'),('4','4'), ('5','5'), ('6','6')), default='1')

# какой предмет кто ведет
class Teaching(models.Model):
    id_teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
