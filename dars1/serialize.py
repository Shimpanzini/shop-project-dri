from rest_framework.serializers import ModelSerializer
from . models import School


class SchoolSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = School


class StudentSerializer(ModelSerializer):
    school = SchoolSerializer(read_only=True)

    class Meta:
        failed = '__all__'
        model = School