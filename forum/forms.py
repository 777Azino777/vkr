from django.forms import ModelForm
from forum.models import Comments,Article
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comments_text'].widget.attrs.update({'class': 'form-control','rows':'3'})


    class Meta:
        model = Comments
        fields = ('comments_text',)


class AddArticle(ModelForm):
    class Meta:
        model = Article
        fields = ('article_title','article_text',)


class MyRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs.update({'type': 'form-control','rows':'3'})


    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Имя пользователя'}))
    password2 = forms.CharField(label='Повторите пароль', required=False,widget=forms.TextInput(attrs={'type':'password'}))
    email = forms.EmailField(required=True, error_messages='')
    #first_name = forms.BooleanField(disabled=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')
        #fields = ('__all__')