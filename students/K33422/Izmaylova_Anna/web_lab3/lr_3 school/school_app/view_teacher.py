from django.shortcuts import render
from rest_framework.views import APIView
from .models import Teacher, Subject, Timetable
from .serializer_teacher import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView

class TeacherAPIView(ListAPIView):
    renderer_class = [TemplateHTMLRenderer]
    template_name = 'teachers_list.html'
    serializer_class = TeacherSerializer

    def get_queryset(self): 
        queryset = Subject.objects.all() # получить все о предметах записи из базы данных 
        params = self.request.query_params # 

        class_id = params.get("class_id", None) # получить значение параметра class_id из запроса
        
        if class_id: # если class_id передали
            # получить расписание 
            queryset1 = Timetable.objects.all() 
            # отфильтровать расписание по class_id
            queryset1 = queryset1.filter(class_id=class_id)
            # отфильтровать предметы, взять только информатику 
            informatics = Subject.objects.all().filter(subject='Информатика').values('id')
            informatics = list(informatics)
            informatics = informatics[0]['id']
            # отфильтровать раписание по информатике, взять учителей
            queryset1 = queryset1.filter(subject_id=informatics).values('teacher_id')
            teacher = list(queryset1)
            teacher = teacher[0]['teacher_id']
            # взять предметы, которые ведут эти учителя
            subjects = queryset.filter(teacher_id=teacher).values('subject')
            subjects = [item["subject"] for item in list(subjects)]
            # взять учителей, которые ведут предметы из предыдущего пункта
            teachers = queryset.filter(subject__in=subjects).values('teacher_id')
            teachers = [item["teacher_id"] for item in list(teachers)]
            # вернуть список учителей
            return Teacher.objects.all().filter(id__in=teachers)

        return Teacher.objects.all()


class TeacherCreateView(CreateAPIView):
    serializer_class = TeacherSerializer
    queryset =  Teacher.objects.all()
    permission_classes = (AllowAny,)

class TeacherDelete(DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherUpdate(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherIDSerializer

