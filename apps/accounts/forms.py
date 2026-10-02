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

    def passwords_match(self) -> bool:
        return self.password == self.confirm_password


class CreateAccountFromInvite(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'flex-1 focus:outline-0'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'flex-1 focus:outline-0', 'x-bind:type': "showPassword ? 'text' : 'password'"})
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'flex-1 focus:outline-0', 'x-bind:type': "showConfirmPassword ? 'text' : 'password'"})
    )

    def passwords_match(self) -> bool:
        return self.password == self.confirm_password


class Login(forms.Form):
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
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'})
    )