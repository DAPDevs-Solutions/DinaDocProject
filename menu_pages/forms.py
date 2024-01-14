from django import forms
from .models import ContactUs


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
        labels = {
            'name':  'Имя',
            'email': 'Email',
            'message': 'Сообщение'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
