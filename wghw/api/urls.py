from django.conf.urls import url

from wghw.api.views import MessagesJSONView, UsersJSONView

urlpatterns = [
    url(r'^users/$', UsersJSONView.as_view(), name='users'),
    url(r'^messages/$', MessagesJSONView.as_view(), name='messages'),
]
