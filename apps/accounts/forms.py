from typing import Any

from django import forms

class CreateOwnerAccount(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'flex-1 focus:outline-0'})
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'flex-1 focus:outline-0', 'placeholder': 'name@example.com'})
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'flex-1 focus:outline-0', 'x-bind:type': "showPassword ? 'text' : 'password'"})
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'flex-1 focus:outline-0', 'x-bind:type': "showConfirmPassword ? 'text' : 'password'"})
    )

    def clean(self) -> dict[str, Any] | None:
        cleaned = super().clean()
        if not cleaned.get('password') == cleaned.get('confirm_password'):
            self.add_error('confirm_password', 'Passwords do not match')
        return cleaned

class CreateAccountFromInvite(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'flex-1 focus:outline-0'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'flex-1 focus:outline-0', 'placeholder': 'name@example.com', 'readonly': True})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'flex-1 focus:outline-0', 'x-bind:type': "showPassword ? 'text' : 'password'"})
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'flex-1 focus:outline-0', 'x-bind:type': "showConfirmPassword ? 'text' : 'password'"})
    )

    def clean(self) -> dict[str, Any] | None:
        cleaned = super().clean()
        if not cleaned.get('password') == cleaned.get('confirm_password'):
            self.add_error('confirm_password', 'Passwords do not match')
        return cleaned


class SignIn(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'flex-1 focus:outline-0', 'placeholder': 'name@example.com'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'flex-1 focus:outline-0', 'x-bind:type': "showPassword ? 'text' : 'password'"})
    )

    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'})
    )

class ForgotPassword(forms.Form):    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'flex-1 focus:outline-0'})
    )

class ResetPassword(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'flex-1 focus:outline-0', 'x-bind:type': "showPassword ? 'text' : 'password'"})
    )
    
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'flex-1 focus:outline-0', 'x-bind:type': "showConfirmPassword ? 'text' : 'password'"})
    )

    def clean(self) -> dict[str, Any] | None:
        cleaned = super().clean()
        if not cleaned.get('password') == cleaned.get('confirm_password'):
            self.add_error('confirm_password', 'Passwords do not match')
        return cleaned