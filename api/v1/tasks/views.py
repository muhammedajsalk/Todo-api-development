from rest_framework.response import Response
from rest_framework.decorators import api_view

from tasks.models import Task
from api.v1.tasks.serializers import TaskSerializer


@api_view(["GET"])
def tasks(request):
    instance = Task.objects.filter(is_deleted=False)
    serializer = TaskSerializer(instance, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        response_data = {
            "status_code" : 6000,
            "message" : "Success"
        }

        return Response(response_data)
    
    else:
        response_data = {
            "status_code" : 6001,
            "message" : "Validation error",
            "data" : serializer.errors
        }
        return Response(serializer.errors)