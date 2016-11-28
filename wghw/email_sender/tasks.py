from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from wghw import celery_app
from wghw.email_sender.models import Message


@celery_app.task
def send_email(username, **kwargs):
    message = render_to_string('email.html', dict(username=username, message=kwargs['text']))
    subject = 'Сообщение через тестовое задание от wargaming.net на позицию Python Developer'

    email_kwargs = {
        'subject': subject,
        'body': message,
        'from_email': settings.FROM_EMAIL,
        'to': [kwargs['email_to']],
    }
    msg = EmailMessage(**email_kwargs)
    msg.content_subtype = 'html'
    msg.send()

    Message.objects.get(pk=kwargs['pk']).set_sended()
