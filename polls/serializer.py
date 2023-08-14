from rest_framework import serializers
from .models import ToDoModel

class ToDoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ToDoModel
        fields = ('id','task_name','task_desc','create_at','update_at','status')