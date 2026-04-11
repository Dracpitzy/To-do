from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import Todoserializer
from .model import Todo 
# Create your views here.
class TodoAPIView(APIView):
  def get():