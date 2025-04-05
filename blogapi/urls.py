from django.urls import path
from .views import (
    api_root,
    RegisterView,
    LoginView,
    BlogPostListCreateView,
    BlogPostRetrieveUpdateDestroyView,
    UserBlogPostsView
)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
    path('my-posts/', UserBlogPostsView.as_view(), name='user-posts'),
]