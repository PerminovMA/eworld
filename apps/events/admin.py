from django.contrib import admin
from models import Order, AuctionOrder, Bet


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status')


@admin.register(AuctionOrder)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status')


admin.site.register(Bet)