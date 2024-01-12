from django import forms
from .models import ContactUs


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
