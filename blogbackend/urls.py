from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'message': 'Welcome to Blog API',
        'endpoints': {
            'admin': '/admin/',
            'api_docs': '/api/',
            'posts': '/api/posts/',
            'auth': '/api/auth/'
        }
    })

urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('api/auth/', include('accounts.urls')),
]