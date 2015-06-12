from django.contrib import admin
from models import Order, AuctionOrder, Bet


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status')


@admin.register(AuctionOrder)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status', 'current_price')


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ('auction', 'owner', 'amount')