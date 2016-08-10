from django import forms
from django.contrib.auth.models import User
import re

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        cd = self.cleaned_data
        match_correct_email_format = re.fullmatch('^.*@alueducation.com$', cd['email'])
        print(cd['email'])
        print(match_correct_email_format)
        if not match_correct_email_format:
            raise forms.ValidationError('Enter an @alueducation.com email address')
        return cd['email']

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)