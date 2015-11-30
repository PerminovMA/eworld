__author__ = 'PerminovMA@live.ru'


from rest_framework.routers import DefaultRouter
from events.rest_api import rest_views

router = DefaultRouter()
router.register(r'auctions_data', rest_views.AuctionOrderView, base_name='auctions_data')
router.register(r'orders_data', rest_views.OrderView, base_name='orders_data')
router.register(r'categories_data', rest_views.CategoryOrderView, base_name='categories_data')