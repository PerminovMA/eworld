# -*- coding: utf-8 -*-

from django import forms
from profiles.models import City
from events.models import Category
from multiupload.fields import MultiFileField

__author__ = 'PerminovMA@live.ru'


class AddEventForm(forms.Form):
    name = forms.CharField(help_text=u"Название проекта")
    event_date = forms.DateField(required=False, help_text=u"Планируемая дата", widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    price = forms.DecimalField(max_digits=8, decimal_places=2, min_value=0, help_text=u"Бюджет")
    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label=u"--Выберите город--", help_text=u"Город")
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), help_text=u"Укажите категории проекта",
                                                widget=forms.CheckboxSelectMultiple)
    files = MultiFileField(min_num=0, max_num=10, max_file_size=1024*1024*10, required=False)
    description = forms.CharField(widget=forms.Textarea, help_text=u"Описание проета")
    requirements = forms.CharField(widget=forms.Textarea, required=False, help_text=u"Требования к проекту")
