from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CustomRegistrationForm(forms.ModelForm):

    password_1 = forms.CharField(required=True, widget=forms.PasswordInput)
    password_2 = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password_1']!=cd['password_2']:
            raise forms.ValidationError('Podane hasła różnią się')
        return cd['password_2']
