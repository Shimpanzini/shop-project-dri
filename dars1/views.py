from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import School, Student
from .serialize import SchoolSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class SchoolApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk=None):
        print(pk)
        if pk:
            try:
                student = Student.objects.get(id=pk)
                ser1 = StudentSerializer(student)
            except:
                return Response({
                    "message": "student not found"
                })
        else:
            students = Student.objects.all()
        ser1 = StudentSerializer(students, many=True)
        return Response(ser1.data)
        
        
        
        if pk:
            try:
                # schools = School.objects.filter(id=pk)
                school = School.objects.get(id=pk)
                ser = SchoolSerializer(school)
            except:
                return Response({
                    "message": "school not found"
                })
        else:
            schools = School.objects.all()
        ser = SchoolSerializer(schools, many=True)
        return Response(ser.data)
    
    def post(self, request):
        data = StudentSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response
    

    def post(self, request):
        data = SchoolSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)
        
        

    
class StudentApiVIew(APIView):

    def put(self, request, pk=None):
            if pk:
                school = School.objects.filter(id=pk).first()
                data = SchoolSerializer(school, data=request.data)
                data = SchoolSerializer(data=request.data)
                if data.is_valid():
                    data.save()
                    return Response({
                        "message": "school updated sucessfully",
                        "data": data.data
                    })
                else:
                    return Response(data.errors)
                
            return Response({
                "message": "school not found"
            })
    def delete(self, request, pk=None):
        if pk:
            try:
                school = School.objects.get(id=pk)
                school.delete
                msg = "school deleted successfully"
            except:
                msg = "school not found"
        return Response({
            "message": msg
        })
    
    def get(self, request):
        students = Student.objects.all()
        ser = StudentSerializer(students, many=True)
        return Response(ser.data)
    
    
    def post(self,request):
        ser = StudentSerializer(data=request.data)
        msg = "ok"
        if ser.is_valid():
            ser.save()
            msg = "created successfuly"
        # else:
            
        return Response({
            "message": msg
        })
class StudentApiVIew(APIView):
    
    def get(self, request):
        students = Student.objects.all()
        ser = StudentSerializer(students, many=True)
        return Response(ser.data)
    
    def post(self, request):
        ser = StudentSerializer(data=request.data)
        msg = "ok"
        if ser.is_valid():
            ser.save()
            msg = "craeted successfully"
        else:
            msg = ser.errors
        return Response({
            "message": msg
        })

class TestApiView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):    
        return Response({
            "message": "hello world"
        })