from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import Todoserializer
from rest_framework import status


@api_view(['GET'])
def list_todos(request):
    todos = Todo.objects.all()
    serializer = Todoserializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_todo(request):
    serializer = Todoserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    serializer = Todoserializer(todo, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
