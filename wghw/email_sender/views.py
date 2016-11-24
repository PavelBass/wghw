from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from email_sender.forms import EmailSendForm


class EmailSendView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'email_send.html'
    form_class = EmailSendForm
    success_url = 'ok'

    def form_valid(self, form):
        #form.send_email()
        return super(EmailSendView, self).form_valid(form)
