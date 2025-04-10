from django.contrib import admin
from django.urls import path, include
from api.views import HelloWorld  # Ensure correct import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('api/', include('api.urls')),  # Ensure 'api.urls' exists
    path('api/exam/chat', include('api.exam.urls')),
]
