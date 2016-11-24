from django.conf.urls import url
from django.views.generic import TemplateView

from email_sender.views import EmailSendView


urlpatterns = [
    url(r'^$', EmailSendView.as_view()),
    url(r'^ok/$', TemplateView.as_view(template_name='email_sended.html')),
]
