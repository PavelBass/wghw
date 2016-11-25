import datetime
from django import forms


class EmailSendForm(forms.Form):
    email = forms.EmailField()
    time = forms.TimeField(widget=forms.TimeInput)
    message = forms.CharField(widget=forms.Textarea)

    def calculate_datetime(self):
        today = datetime.date.today()
        time = self.cleaned_data['time']
        return datetime.datetime.combine(today, time)
