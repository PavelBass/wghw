from django.conf.urls import url
from api.views import UsersView

urlpatterns = [
    url(r'^users/$', UsersView.as_view()),
]
