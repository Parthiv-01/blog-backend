from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'message': 'Welcome to the Blog API',
        'endpoints': {
            'posts': '/api/posts/',
            'admin': '/admin/',
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # Your blog app URLs
    path('', api_root),  # Show API welcome instead of Django default
]