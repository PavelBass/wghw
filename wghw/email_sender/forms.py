from django import forms


class EmailSendForm(forms.Form):
    email = forms.EmailField()
    time = forms.TimeField(widget=forms.TimeInput)
    message = forms.CharField(widget=forms.Textarea)
