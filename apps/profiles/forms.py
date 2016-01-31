# -*- coding: utf-8 -*-

from django import forms
from models import UserProfile
from django.utils.translation import ugettext as _

__author__ = 'PerminovMA@live.ru'


class RegistrationForm(forms.Form):
    CLIENT_LABEL = 'client'
    EVENT_MANAGER_LABEL = 'event_manager'

    username = forms.CharField(help_text="Username", max_length=30)
    first_name = forms.CharField(help_text="Имя", required=False)
    last_name = forms.CharField(help_text="Фамилия", required=False)
    email = forms.EmailField(help_text="Электронная почта")
    phone_number = forms.CharField(max_length=15, required=False, help_text="Телефон")
    user_type = forms.ChoiceField(
        choices=[(CLIENT_LABEL, u'Клиент'), (EVENT_MANAGER_LABEL, u'Организатор мероприятий')],
        initial='client', widget=forms.RadioSelect, required=True)
    password = forms.CharField(max_length=128, help_text="Пароль", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserProfile.objects.filter(email=username).last():
            raise forms.ValidationError(_(u"Пользователь с таким именем уже зарегистрирован."),
                                        code="user_already_exist")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.objects.filter(email=email).last():
            raise forms.ValidationError(_(u"Пользователь с такой электронной почтой уже зарегистрирован."),
                                        code="user_already_exist")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError(_(u"Минимальная длинна пароля 6 символов"), code="bad_password")
        return password

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        phone_number = cleaned_data.get("phone_number")
        if phone_number == '':
            cleaned_data["phone_number"] = None


class EmailAuthorizationForm(forms.Form):
    email = forms.EmailField(help_text="Электронная почта")
    password = forms.CharField(max_length=128, help_text="Пароль", widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not UserProfile.objects.filter(email__iexact=email).last():
            raise forms.ValidationError(_(u"Пользователь с такой электронной почтой не зарегистрирован."),
                                        code="user_not_exist")
        return email
