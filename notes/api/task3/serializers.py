from rest_framework.serializers import ModelSerializer
from api.task3.models import Post, Comment

class PostSerializers(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class CommentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"