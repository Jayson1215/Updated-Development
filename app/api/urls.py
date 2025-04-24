# api/urls.py
from django.urls import path
from .views import HelloWorld, Students, ContactListView, ProductListCreateView  # Import the Product view
from .exam_views import ChatView

urlpatterns = [
    path('hello/', Students.as_view(), name='hello_world'),
    path('contact/', Students.as_view(), name='contact_new'),
    path('students/', Students.as_view(), name='list_student'),
    path('api/contact/', Students.as_view(), name='contact'),
    path('exam/', ChatView.as_view(), name='chat_view'),
    path('product/', ProductListCreateView.as_view(), name='product_list_create'),
]
