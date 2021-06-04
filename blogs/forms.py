from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=200)
    email = forms.EmailField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    