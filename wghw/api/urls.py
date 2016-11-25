from django.conf.urls import url
from wghw.api.views import UsersView

urlpatterns = [
    url(r'^users/$', UsersView.as_view()),
]
