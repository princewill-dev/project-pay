from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class CustomEmailField(forms.EmailField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email address',
        })

class CustomPasswordField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })

class CustomAuthenticationForm(AuthenticationForm):
    username = CustomEmailField(label='Email')
    password = CustomPasswordField(label='Password')

    class Meta:
        model = User
        fields = ('email', 'password')

class CustomUserCreationForm(UserCreationForm):
    email = CustomEmailField(label='Email')
    password1 = CustomPasswordField(label='Password')
    password2 = CustomPasswordField(label='Confirm Password')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')