from django.conf.urls import url

from wghw.api.views import MessagesJSONView, UsersJSONView

urlpatterns = [
    url(r'^users/$', UsersJSONView.as_view()),
    url(r'^messages/$', MessagesJSONView.as_view()),
]
