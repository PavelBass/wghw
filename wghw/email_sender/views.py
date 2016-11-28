from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from wghw.email_sender.forms import EmailSendForm
from wghw.email_sender.tasks import send_email


class EmailSendView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'email_send.html'
    form_class = EmailSendForm
    success_url = 'ok/'

    def form_valid(self, form):
        new_message = form.save(commit=False)
        new_message.user = self.request.user
        new_message.save()

        kwargs = form.cleaned_data
        kwargs['pk'] = new_message.pk

        send_email.apply_async(
            args=(new_message.user.username,),
            kwargs=form.cleaned_data,
            eta=form.calculate_datetime(),
        )
        return super(EmailSendView, self).form_valid(form)
