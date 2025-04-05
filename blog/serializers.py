from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']
    
    def get_author(self, obj):
        from accounts.serializers import UserBriefSerializer
        return UserBriefSerializer(obj.author).data