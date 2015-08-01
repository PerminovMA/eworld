__author__ = 'PerminovMA@live.ru'

from rest_framework import serializers
from events.models import AuctionOrder


class AuctionOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionOrder
        # fields = ()