

from django.urls import path
from .views import posts_list, posts_detail


urlpatterns = [
    path('posts/', posts_list),
    path('posts/<int:pk>/comments', posts_detail)
]
