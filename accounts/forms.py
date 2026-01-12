from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

TAILWIND_INPUT = (
    "w-full px-4 py-2 border border-gray-300 rounded-lg "
    "focus:outline-none focus:ring-2 focus:ring-blue-500 "
    "focus:border-blue-500"
)

TAILWIND_LABEL = "block text-sm font-medium text-gray-700 mb-1"


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, label='Email', widget=forms.EmailInput(attrs={'class': TAILWIND_INPUT, 'placeholder': 'Email Address'}))
    username = forms.CharField(
        label='Username', widget=forms.TextInput(attrs={'class': TAILWIND_INPUT, 'placeholder': 'Enter Username'}))
    password1 = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'class': TAILWIND_INPUT, 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': TAILWIND_INPUT, 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Apply Tailwind classes to labels
            for field in self.fields.values():
                field.label_suffix = ""


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": TAILWIND_INPUT,
            "placeholder": "Username"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": TAILWIND_INPUT,
            "placeholder": "Password"
        })
    )