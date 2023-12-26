from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer



# Create your views here.


@api_view(['GET'])
def api_overview(request):
    api_urls={
        'List':'/task-list/',
        'Detail': '/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>'
    }
    return Response(api_urls,status=status.HTTP_200_OK)


@api_view(['GET'])
def taskList(request):
    task=Task.objects.all()
    serializer=TaskSerializer(task,many=True)
    return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def taskDetail(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(task,many=False)
    return Response(serializer.data,status=status.HTTP_302_FOUND)


@api_view(['POST'])
def taskCreate(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['POST','PUT'])
def taskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'msg':'Data is Updated'}, status=status.HTTP_205_RESET_CONTENT)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response({'msg':'Data is Deleted'})