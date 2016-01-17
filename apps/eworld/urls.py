__author__ = 'PerminovMA@live.ru'

from django.views.generic import TemplateView
from django.conf.urls import patterns, url, include
from events.rest_api.api_router import router
from eworld import views

urlpatterns = patterns('',
                       url(r'dashboard', TemplateView.as_view(template_name='eworld/dashboard.html'), name='dashboard'),

                       url(r'my_auctions_list', TemplateView.as_view(template_name='eworld/my_auctions_list.html'),
                           name='my_auctions_list'),
                       url(r'auctions_list', TemplateView.as_view(template_name='eworld/auctions_list.html'),
                           name='auctions_list'),
                       url(r'single_auction/(?P<auction_id>[0-9]?)', views.single_auction,
                           name='single_auction'),

                       url(r'my_orders_list', TemplateView.as_view(template_name='eworld/my_orders_list.html'),
                           name='my_orders_list'),
                       url(r'orders_list', TemplateView.as_view(template_name='eworld/orders_list.html'),
                           name='orders_list'),
                       url(r'single_order/(?P<order_id>[0-9]?)', views.single_order,
                           name='single_order'),

                       url(r'rest_api/', include(router.urls, namespace='rest_api_urls')),
                       )
