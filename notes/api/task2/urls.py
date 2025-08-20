

from django.urls import path
from .views import tasks, task_detail


urlpatterns = [
    path('tasks/', tasks),
    path('tasks/<int:pk>/', task_detail)
]
