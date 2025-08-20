

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.task2.models import Task
from api.task2.serializers import Task2Serializers 

@api_view(['GET', 'POST'])
def tasks(request):
    if request.method == 'GET':
        completed = request.query_params.get('completed')
        tasks = Task.objects.all()
        if completed is not None:
            tasks = tasks.filter(completed=completed.lower() == 'true')
        serializer = Task2Serializers(tasks, many=True)
        return Response(serializer.data)
    
    elif request.metthod == 'POST':
        serializer = Task2Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = Task2Serializers(task)
    return Response(serializer.data)
