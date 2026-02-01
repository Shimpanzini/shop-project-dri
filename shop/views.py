from rest_framework.views import APIView
from rest_framework.response import Responce
from .models import Category
from .serializer import  CategorySerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class Mypagiantor(PageNumberPagination):
    page_size = 40
    


class CategoryAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("-created_at")
    pagination_class = Mypagiantor
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'is_active', 'parent', 'created_at']
    search_fields = ['name']