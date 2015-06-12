from django.contrib import admin
from models import Order, AuctionOrder, Bet, Category


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status')


@admin.register(AuctionOrder)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status', 'get_best_bet')
    readonly_fields = ('bets_list',)

    def bets_list(self, instance):
        from django.utils.html import format_html_join
        from django.utils.safestring import mark_safe

        return format_html_join(
            mark_safe('<br/>'),
            '{}',
            ((line,) for line in instance.bet_set.order_by('amount')),
        ) or "<span class='errors'>No bets.</span>"

    bets_list.short_description = "Bets of this auction"
    bets_list.allow_tags = True


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ('auction', 'owner', 'amount')


@admin.register(Category)
class BetAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_percent', 'auction_percent')