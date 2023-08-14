from django.urls import path
from .views import (get_all, get_index, Email, CreateToDo,
                    Delete, Update)

urlpatterns = [
    path('get_all/', get_all.as_view()),
    path('get_index/<int:get_id>', get_index.as_view()),
    path('name/<str:nam>', Email.as_view()),
    path('create/', CreateToDo.as_view()),
    path('delete/<int:id>', Delete.as_view()),
    path('update/<int:id>', Update.as_view()),
]
