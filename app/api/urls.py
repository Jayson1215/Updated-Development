from django.urls import path
from .import views
from .views import HelloWorld
from .views import Students
from .views import ContactListView
from .exam_views import ChatView

urlpatterns = [
    path('hello/', Students.as_view(), name='hello_world'),
    path('contact/', Students.as_view(), name='contact_new'),
    path('students/', Students.as_view(), name='list_student'),
    path('api/contact/', Students.as_view(), name='contact'),
    path('exam/', ChatView.as_view(), name='chat_view'),
]
