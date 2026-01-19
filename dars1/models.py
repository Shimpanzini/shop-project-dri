from django.db import models

# Create your models here.
class SchoolType(models.TextChoices):
    davlat = "davlat", "davlat maktabi"
    xususiy = "xususiy", "Xususiy maktab"

class School(models.Model):

    name = models.CharField(max_length=255)
    students_count = models.IntegerField(default=0)
    school_type = models.CharField(max_length=50, choices=SchoolType.choices, default=SchoolType.davlat)
    director_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    class GradeChoices(models.TextChoices):
        GRADE1 = ("grade1", "1-sinf")
        GRADE2 = ("grade2", "2-sinf")
        GRADE3 = ("grade3", "3-sinf")
        GRADE4 = ("grade4", "4-sinf")
        GRADE5 = ("grade5", "5-sinf")
        GRADE6 = ("grade6", "6-sinf")
        GRADE7 = ("grade7", "7-sinf")
        GRADE8 = ("grade8", "8-sinf")
        GRADE9 = ("grade9", "9-sinf")
        GRADE10 = ("grade10", "10-sinf")
        GRADE11 = ("grade11", "11-sinf")
        GRADE12 = ("grade12", "12-sinf")
        
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=40, 
        choices=GradeChoices.choices, default=GradeChoices.GRADE1)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    joined_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
