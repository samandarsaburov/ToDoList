from django.db import models
from datetime import datetime
# # Create your models here.
class ToDoModel(models.Model):
    # id = models.IntegerField()
    task_name = models.CharField(default='', max_length=25)
    task_desc = models.TextField()
    create_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.task_name
    
    class Meta:
        db_table = 'todo'