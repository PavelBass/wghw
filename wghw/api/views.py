from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User

from wghw.celery_application import app


class UsersJSONView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.values('username', 'date_joined')
        result = {'users': list(users)}
        return JsonResponse(result)


class TasksJSONView(View):
    def get(self, request, *argd, **kwargs):
        inspect = app.control.inspect()
        tasks = []
        result = {'tasks': tasks, 'scheduled': repr(inspect.scheduled()), 'active': repr(inspect.active())}
        return JsonResponse(result)
