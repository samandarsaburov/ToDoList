from django.contrib import admin
from .models import ToDoModel

# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['task_name','task_desc','create_at','update_at','status']
    search_fields = ['task_name']
admin.site.register(ToDoModel,ToDoAdmin)