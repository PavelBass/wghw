from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/email_send/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
