from django.shortcuts import render
from .models import ToDoModel
from .serializer import ToDoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED
# Create your views here.

class get_all(APIView):
    def get(self, request, *args , **kwargs):
        all_data = ToDoModel.objects.all()
        serializer = ToDoSerializer(all_data, many=True)
        return Response(serializer.data)     
    # end def
    
    
class get_index(APIView):
    def post(self, request, *args , **kwargs):
        ToDoId = kwargs['get_id']
        ToDo = get_object_or_404(ToDoModel, id = ToDoId)
        serializer = ToDoSerializer(ToDo)
        return Response(serializer.data)
    # end def
    

class Email(APIView):
    def post(self, request, *args, **kwargs):
        name = kwargs['nam']
        todo = get_object_or_404(ToDoModel,  task_name = name)
        serializer  = ToDoSerializer(todo)
        return Response(serializer.data)
    # end def
    
class CreateToDo(APIView):
    def post(self,request,*args,**kwargs ):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)
    
class Delete(APIView):
    def delete(self,request,*args,**kwargs):
        ToDo_id = kwargs['id']
        ToDo = get_object_or_404(ToDoModel, id= ToDo_id)
        ToDo.delete()
        return Response({'msg':'deleted'})
    # end def
    
    
    # valusini ozgartirish 
class Update(APIView):
    def patch(self, request,*args,**kwargs):
        todo = get_object_or_404(ToDoModel, id = kwargs['id'])
        serializer = ToDoSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)