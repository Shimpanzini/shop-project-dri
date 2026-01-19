from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import School, Student
from .serialize import SchoolSerializer, StudentSerializer
# Create your views here.


class SchoolApiView(APIView):

    def get(self, request):
        schools = School.objects.all()
        ser = SchoolSerializer(schools, many=True)
        return Response(ser.data)
    
class StudentApiVIew(APIView):
    
    def get(self, request):
        students = Student.objects.all()
        ser = StudentSerializer(students, many=True)
        return Response(ser.data)
    
    def post(self,request):
        ser = StudentSerializer(request.data)
        msg = "ok"
        if ser is_valid():
            ser.save()
            msg = "created successfuly"
        return Response({
            "message": msg
        })
