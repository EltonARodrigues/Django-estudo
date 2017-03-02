from django import forms
from django.models import Users


class UserForm(forms.ModelForm):
    Usuario = forms.CharField(label='Your name', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Users
