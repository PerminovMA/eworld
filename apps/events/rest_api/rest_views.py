__author__ = 'PerminovMA@live.ru'

from events.rest_api.serializers import AuctionOrderSerializer, CategorySerializer
from events.models import AuctionOrder, Category
from rest_framework import viewsets
from rest_framework import permissions
import datetime


class AuctionOrderView(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuctionOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        selected_order_type_id = self.request.GET.get('selectedOrderType')
        sort_order = self.request.GET.get('sortOrder')
        selected_city = self.request.GET.get('selectedCity')

        auctions_set = AuctionOrder.objects.all()

        if selected_city:
            auctions_set = auctions_set.filter(city__name=selected_city)
        if selected_order_type_id:
            auctions_set = auctions_set.filter(categories=selected_order_type_id)

        if sort_order:
            if sort_order == 'this_day':
                today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
                today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
                auctions_set = auctions_set.filter(creation_datetime__range=(today_min, today_max))
            elif sort_order == 'this_week':
                auctions_set = auctions_set.filter(
                    creation_datetime__range=(datetime.datetime.now() - datetime.timedelta(7), datetime.datetime.now()))
            elif sort_order == 'by_newest':
                auctions_set = auctions_set.order_by('-creation_datetime')

        return auctions_set


class CategoryOrderView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated,)