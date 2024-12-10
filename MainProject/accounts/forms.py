from django import forms
from .models import *
class LoginForm(forms.ModelForm):
    class Meta:
        model = Contributor
        fields = ['username','password']

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=40,widget=forms.PasswordInput(
        attrs={
            'placeholder':'Enter Password',
        }
    ))
    class Meta:
        model = Contributor
        exclude = ['is_superuser','is_staff']