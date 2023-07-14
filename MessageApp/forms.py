from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from BlogApp.models import Blog, Profile
from MessageApp.models import Message


class NewMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'message_body', 'to_user', 'date']
        widgets = {
            'date': forms.DateInput(format='%d/%m/%Y'),
            'from_user': forms.HiddenInput(),
        }
        labels = {
            'title': 'Título del mensaje',
            'message_body': 'Mensaje',
            'to_user': 'Para',
            'date': 'Fecha',
        }


