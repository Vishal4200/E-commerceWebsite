from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Enter Password Here...'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Confirm Password...'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'dob': DateInput(),
        }
        exclude = ('user',)