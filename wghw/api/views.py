from django.http import JsonResponse
from django.views.generic import View

from wghw.email_sender.models import Message, User


class UsersJSONView(View):
    def get(self, *args, **kwargs):
        result = {'users': User.get_users_list()}
        return JsonResponse(result)


class MessagesJSONView(View):
    def get(self, request, *argd, **kwargs):
        status = request.GET.get('status')
        tasks = Message.get_messages_list(status)
        result = {'messages': list(tasks)}
        return JsonResponse(result)
