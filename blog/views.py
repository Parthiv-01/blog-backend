from rest_framework import generics, permissions
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]