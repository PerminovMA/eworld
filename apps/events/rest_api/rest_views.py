__author__ = 'PerminovMA@live.ru'

from events.rest_api.serializers import AuctionOrderSerializer, CategorySerializer, OrderSerializer, BetSerializer
from events.models import AuctionOrder, Category, Order, Bet
from rest_framework import viewsets
from rest_framework import permissions
import datetime
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route


class AuctionOrderView(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuctionOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        get_only_my_auctions = self.request.GET.get('get_only_my_auctions')
        if get_only_my_auctions and get_only_my_auctions == 'true':
            if self.request.user.is_client:
                return self.request.user.client.auctionorder_set.all()
            else:
                return []

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

    @list_route()
    def best_bets(self, request):
        auction_id = self.request.GET.get('auction_id')
        auction = get_object_or_404(AuctionOrder, pk=auction_id)
        bets_queryset = auction.get_best_bet(5)
        serializer = BetSerializer(bets_queryset, many=True)
        return Response(serializer.data)


class OrderView(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        get_only_my_orders = self.request.GET.get('get_only_my_orders')
        if get_only_my_orders and get_only_my_orders == 'true':
            if self.request.user.is_client:
                return self.request.user.client.order_set.all()
            else:
                return []

        return Order.objects.all()


class CategoryOrderView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
