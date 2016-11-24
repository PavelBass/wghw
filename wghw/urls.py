from django.conf.urls import url, include
from django.contrib import admin

from auth.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # auth
    url('^', include('django.contrib.auth.urls')),
    url(r'^registration/$', RegistrationView.as_view()),

    # email send
    url(r'^email_send/', include('email_sender.urls', namespace='email_send')),

    # api
    url(r'^api/', include('api.urls', namespace='api')),

]
