from events.models import AuctionOrder, Order
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.contrib.contenttypes.models import ContentType
from eworld.models import Attach


def single_auction(request, auction_id):
    auction_order = get_object_or_404(AuctionOrder, pk=auction_id)
    auction_categories = auction_order.categories.values_list('name', flat=True)

    auction_content_type = ContentType.objects.get_for_model(auction_order)
    auction_attaches = Attach.objects.filter(content_type__pk=auction_content_type.id, object_id=auction_order.id)
    if auction_order.min_price is None:
        auction_order.min_price = auction_order.start_price / 2

    context = {"auction_order": auction_order,
               "auction_categories": auction_categories,
               "auction_attaches": auction_attaches}
    return render(request, 'eworld/single_auction.html', context)


def single_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_categories = order.categories.values_list('name', flat=True)

    order_content_type = ContentType.objects.get_for_model(order)
    order_attaches = Attach.objects.filter(content_type__pk=order_content_type.id, object_id=order.id)

    context = {"order": order, "order_attaches": order_attaches, "order_categories": order_categories}
    return render(request, 'eworld/single_order.html', context)
