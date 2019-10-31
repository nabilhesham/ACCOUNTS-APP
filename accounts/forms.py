from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username Or Email'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Enter Password Here ..'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Your Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Your Password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password :
            raise forms.ValidationError('Passwords Mismatch')
        return confirm_password

class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
