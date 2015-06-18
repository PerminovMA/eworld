__author__ = 'PerminovMA@live.ru'

from django import forms


class RegistrationForm(forms.Form):
    # спросить

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=False)
    password = forms.CharField(max_length=128)


class EmailAuthorizationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=128)