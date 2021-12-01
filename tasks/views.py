from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.response import Response
from tasks.models import Task
from tasks.seralizers import TaskSerializer


class TaskAPIView(APIView):

    def get(self,request):
        tasks = Task.objects.all()

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)

    def post(self,request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            body = serializer.validated_data.get('body')
            estimated_finish_time = serializer.validated_data.get('estimated_finish_time')
            task = Task.objects.create(body=body, estimated_finish_time=estimated_finish_time)
            serializer = TaskSerializer(instance=task)
            return Response(serializer.data)

        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



    # def put(self,request,id):
    #     task = get_object_or_404(Task, id=id)
    #     serializer = TaskSerializer(instance=task, data=request.data)
    #
    #     if serializer.is_valid():
    #         body = serializer.validated_data.gte('body')
    #         est = serializer.validates_data.get('estimated_finish_time')
    #         task.body = body
    #         task.estimated_finish_time = est
    #         task.save()
    #         return Response(serializer.data)
    #     return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
