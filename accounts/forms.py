from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError('Please confirm your password')

        if password1 != password2:
            raise ValidationError('Passwords must match')

        return password2


class ChangePasswordForm(forms.Form):
    """Form to be used to change password"""
    password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_confirm_password(self):
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if not new_password or not confirm_password:
            raise ValidationError('Please confirm your new password')

        if new_password != confirm_password:
            raise ValidationError('Passwords must match')

        return confirm_password
