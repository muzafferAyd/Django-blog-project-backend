from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("username", "email") 


    def clean_email(self):
        email = self.cleaned_data['email'] 
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Please use another Email, that one alreadey taken")
        return email

        