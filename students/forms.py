from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role')
        widgets = {
            'role': forms.Select(choices=User.Role.choices)
        }

class CustomAuthenticationForm(AuthenticationForm):
    pass