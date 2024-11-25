from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    cpassword = forms.CharField(widget=forms.PasswordInput, label='Confirm password')
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=80, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_cpassword(self):
        cd = self.cleaned_data
        if cd['password'] != cd['cpassword']:
            raise forms.ValidationError('Password don\'t match')
        return cd['cpassword']
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email already exists")
        return data
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)

        if qs.exists():
            raise forms.ValidationError("Email exists already")
        return data

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']