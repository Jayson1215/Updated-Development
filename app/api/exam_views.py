import json
from django.http import JsonResponse
from django.views import View
from .exam_models import Chat

class ChatView(View):
    def get(self, request):
        chats = Chat.objects.all()
        chat_data = [
            {
                "username": chat.username,
                "chat_message": chat.chat_message,
                "date": chat.date.isoformat()
            }
            for chat in chats
        ]
        return JsonResponse(chat_data, safe=False)

    def post(self, request):
        # Parse the incoming JSON request body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)

        username = data.get('username')
        chat_message = data.get('chat_message')

        if username and chat_message:
            new_chat = Chat.objects.create(username=username, chat_message=chat_message)
            chat_data = {
                "username": new_chat.username,
                "chat_message": new_chat.chat_message,
                "date": new_chat.date.isoformat()
            }
            return JsonResponse(chat_data, status=201)  # Updated status code to 201 for successful creation
        return JsonResponse({"error": "Username and message are required."}, status=400)