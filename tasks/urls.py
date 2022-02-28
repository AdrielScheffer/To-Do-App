from django.urls import path
from .views import Index, Create_tasks, Eliminate_task

urlpatterns = [
    path('', Index.as_view(), name = 'home'),
    path('create_task/',Create_tasks.as_view(), name= 'task_creation' ),
    path('tasks/<int:pk>/delete', Eliminate_task.as_view(), name = 'delete')
]