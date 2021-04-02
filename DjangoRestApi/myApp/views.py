from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myApp.models import Student
from myApp.serializers import StudentSerializer

class StudentView(APIView):

    def get(self,request):
        s=Student.objects.all()
        serializer=StudentSerializer(s, many=True)
        return Response(serializer.data)

    def post(self,request):
        pass
