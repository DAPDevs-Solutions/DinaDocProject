from django import forms
from .models import ContactUs
from django.utils.translation import gettext_lazy as _


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
        labels = {
            'name':  _('Имя'),
            'email': _('Email'),
            'message': _('Сообщение')
        }
