from django.contrib.auth.models import User as DjangoUser
from django.db import models


class User(DjangoUser):
    class Meta:
        proxy = True

    @classmethod
    def get_users_list(cls):
        users = cls.objects.values('username', 'date_joined')
        return list(users)


class Message(models.Model):
    user = models.ForeignKey(User)
    email_to = models.EmailField()
    text = models.TextField()
    time = models.TimeField()
    is_sended = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return 'Message {}: "{}" - {}'.format(
            self.pk,
            self.text,
            self.is_sended and 'Отправлено' or 'Ожидает'
        )

    def set_sended(self):
        self.is_sended = True
        self.save()

    @classmethod
    def get_messages_list(cls):
        messages = cls.objects.values('text', 'is_sended')
        messages = [{
                        'text': message['text'],
                        'status': message['is_sended'] and 'Отправлено' or 'Ожидает'
                    } for message in messages]
        return messages
