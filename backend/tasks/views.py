from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView,
    RetrieveAPIView,  
    UpdateAPIView, 
    DestroyAPIView
)
from .models import Task
from .serializers import TasksSerializer
from rest_framework import permissions


class ListTasksView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Task.objects.all()
    serializer_class = TasksSerializer


class CreateTaskAPIView(CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    

class RetrieveTasksView(RetrieveAPIView):
    queryset = Task.objects.order_by('-created')
    serializer_class = TasksSerializer
    lookup_field = 'slug'
    
    
class UpdateTasksView(UpdateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    lookup_field = 'slug'


class DeleteAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    lookup_field = 'slug'
    

class SearchView(APIView):
    #permission_classes = (permissions.AllowAny, )
    serializer_class = TasksSerializer

    def post(self, request, format=None):
        queryset = Task.objects.order_by('-created')
        data = self.request.data

        title = data['title']
        queryset = queryset.filter(title__iexact=title)
        
        created = data['created']
        queryset = queryset.filter(created__iexact=created)
        




"""
class TasksView(RetrieveAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
"""    
    
