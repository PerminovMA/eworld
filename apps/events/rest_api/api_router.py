__author__ = 'PerminovMA@live.ru'


from rest_framework.routers import DefaultRouter, SimpleRouter
from events.rest_api import rest_views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'auctions_data', rest_views.AuctionOrderView, base_name='auctions_data')


# urlpatterns = [
#     url(r'auction_orders', rest_views.AuctionOrderView.as_view()),
#     # url(r'^offers/$', OffersList.as_view()),
#     # url(r'^adv_campaigns/$', AdvCampaignsList.as_view()),
#     # url(r'^adv_campaign/(?P<pk>[0-9]+)/$', AdvCampaignDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)