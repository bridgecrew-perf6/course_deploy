from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Course
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, Category, Branch, Contact
from .serializers import CourseSerializer, ContactSerializers, CategorySerializers, BranchSerializer
from rest_framework import generics



def home(request):
    course = Course.objects.all()
    branch = Branch.objects.all()
    contact = Contact.objects.all()
    return render(request, 'courses/home.html', {'course': course, 'branch': branch, 'contact': contact})




class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_queryset(self):
        return Course.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = CategorySerializers


class BranchView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer