__author__ = 'PerminovMA@live.ru'

from django.views.generic import TemplateView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name='eworld/index.html'), name='index'), )