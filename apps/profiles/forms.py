# -*- coding: utf-8 -*-

__author__ = 'PerminovMA@live.ru'

from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(help_text="Имя")
    last_name = forms.CharField(help_text="Фамилия")
    email = forms.EmailField(help_text="Электронная почта")
    phone_number = forms.CharField(max_length=15, required=False, help_text="Телефон")
    password = forms.CharField(max_length=128, help_text="Пароль")


class EmailAuthorizationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=128)