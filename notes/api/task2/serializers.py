

from rest_framework.serializers import ModelSerializer
from api.task2.models import Task

class Task2Serializers(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
