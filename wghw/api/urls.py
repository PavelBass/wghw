from django.conf.urls import url
from wghw.api.views import UsersJSONView, TasksJSONView

urlpatterns = [
    url(r'^users/$', UsersJSONView.as_view()),
    url(r'^messages/$', TasksJSONView.as_view()),

]
