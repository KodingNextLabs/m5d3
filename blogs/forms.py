from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField()

    def send_email(self):
        pass


class RegisterForm(forms.Form):
    LEVEL_CHOICES = (
        ("1", 'Superadmin'),
        ("2", 'User Staff'),
        ("3", 'User Biasa')
    )
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=200)
    email = forms.EmailField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    level = forms.ChoiceField(choices=LEVEL_CHOICES, initial="2")



class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(), max_length=200)
    confirm = forms.CharField(widget=forms.PasswordInput(), max_length=200)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('new_password') != cleaned_data.get('confirm'):
            raise forms.ValidationError('Password tidak sama!')
        
        return cleaned_data