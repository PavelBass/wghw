from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from wghw.email_sender.forms import EmailSendForm
from wghw.email_sender.tasks import send_email


class EmailSendView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'email_send.html'
    form_class = EmailSendForm
    success_url = 'ok/'

    def form_valid(self, form):
        send_email.apply_async(
            args=(self.request.user.username,),
            kwargs=form.cleaned_data,
            eta=form.calculate_datetime(),
        )
        return super(EmailSendView, self).form_valid(form)
