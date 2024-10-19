from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=8)
    repeat_password = forms.CharField(max_length=8)
    age = forms.CharField(max_length=3)
