__author__ = 'PerminovMA@live.ru'

from rest_framework import serializers
from events.models import AuctionOrder
from events.models import Category
from profiles.rest_api.serializers import ClientSerializer, CitySerializer


class AuctionOrderSerializer(serializers.ModelSerializer):
    owner = ClientSerializer()
    city = CitySerializer()
    order_views_count = serializers.SerializerMethodField('order_views_counter')
    best_bet = serializers.SerializerMethodField()

    def order_views_counter(self, auction):
        return auction.order_views.count()

    def get_best_bet(self, auction):
        best_bests = auction.get_best_bet()
        if best_bests:
            return best_bests[0].amount
        else:
            return None

    class Meta:
        model = AuctionOrder
        # exclude = ('order_views',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category