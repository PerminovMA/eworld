__author__ = 'PerminovMA@live.ru'

from rest_framework import serializers
from events.models import AuctionOrder, Order, OrderComment, Category, Bet
from profiles.rest_api.serializers import ClientSerializer, CitySerializer, UserProfileShortSerializer


class BaseOrderSerializer(serializers.ModelSerializer):
    order_views_count = serializers.SerializerMethodField('order_views_counter')
    owner = ClientSerializer()
    city = CitySerializer()

    def order_views_counter(self, some_order):
        return some_order.order_views.count()


class AuctionOrderSerializer(BaseOrderSerializer):
    best_bet = serializers.SerializerMethodField()

    def get_best_bet(self, auction):
        best_bests = auction.get_best_bet()
        if best_bests:
            return best_bests[0].amount
        else:
            return None

    class Meta:
        model = AuctionOrder


class OrderSerializer(BaseOrderSerializer):
    class Meta:
        model = Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class BetSerializer(serializers.ModelSerializer):
    owner = ClientSerializer()

    class Meta:
        model = Bet


class CommentSerializer(serializers.ModelSerializer):
    owner = UserProfileShortSerializer()

    class Meta:
        model = OrderComment