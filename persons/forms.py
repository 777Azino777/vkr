from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from persons.models import anonim_message

class An_form(ModelForm):
    nickname_message = forms.CharField(label='Псевдоним')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_message'].widget.attrs.update({'class': 'form-control','rows':'3'})
        self.fields['nickname_message'].widget.attrs.update({'class': 'form-group mx-sm-3 mb-2'})


    class Meta:
        model = anonim_message
        fields = ('text_message','nickname_message',)
