__author__ = 'PerminovMA@live.ru'

from django.views.generic import TemplateView
from django.conf.urls import patterns, url, include
from events.rest_api.api_router import router

urlpatterns = patterns('',
                       url(r'dashboard', TemplateView.as_view(template_name='eworld/dashboard.html'), name='dashboard'),

                       url(r'my_auctions_list', TemplateView.as_view(template_name='eworld/my_auctions_list.html'),
                           name='my_auctions_list'),
                       url(r'auctions_list', TemplateView.as_view(template_name='eworld/auctions_list.html'),
                           name='auctions_list'),

                       url(r'my_orders_list', TemplateView.as_view(template_name='eworld/my_orders_list.html'),
                           name='my_orders_list'),
                       url(r'orders_list', TemplateView.as_view(template_name='eworld/orders_list.html'),
                           name='orders_list'),

                       url(r'rest_api/', include(router.urls, namespace='rest_api_urls')),
                       )