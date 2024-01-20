from django import forms
from .models import ContactUs
from django.utils.translation import gettext_lazy as _


class FeedbackForm(forms.ModelForm):
    # name = forms.CharField(label=_('Name'))
    # email = forms.EmailField(label=_('Email'))
    # message = forms.CharField(label=_('Message'), widget=forms.Textarea)

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
        labels = {
            'name':  'Имя',
            'email': 'Email',
            'message': 'Сообщение'
        }
