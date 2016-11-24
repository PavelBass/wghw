from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User


class UsersView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.values('username', 'date_joined')
        result = {
            'users': [user for user in users],
        }
        return JsonResponse(result)
