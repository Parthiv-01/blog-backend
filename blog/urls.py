from django.urls import path
from .views import BlogPostListCreateView, BlogPostRetrieveUpdateDestroyView

urlpatterns = [
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
]