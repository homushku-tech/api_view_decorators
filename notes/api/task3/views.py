from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.task3.models import Post, Comment
from api.task3.serializers import PostSerializers, CommentSerializers
@api_view(['GET', 'POST'])
def posts_list(requests):
    if requests.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many = True)
        return Response(serializer.data)
    elif requests.method == 'POST':
        serializer = PostSerializers(data = requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def posts_detail(requests, pk):
    if requests.method == 'GET':
        comments = Comment.objects.filter(post = pk)
        serializer = CommentSerializers(comments, many = True)
        return Response(serializer.data)
