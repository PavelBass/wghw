import datetime

from django import forms

from wghw.email_sender.models import Message


class EmailSendForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['email_to', 'time', 'text']
        widgets = {
            'text': forms.Textarea(),
        }

    def calculate_datetime(self):
        today = datetime.date.today()
        time = self.cleaned_data['time']
        return datetime.datetime.combine(today, time)
