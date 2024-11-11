from django import forms
from django.contrib.auth.models import User

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