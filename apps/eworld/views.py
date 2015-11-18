from events.models import AuctionOrder
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.contrib.contenttypes.models import ContentType
from eworld.models import Attach


def single_auction(request, auction_id):
    auction_order = get_object_or_404(AuctionOrder, pk=auction_id)
    auction_categories = auction_order.categories.values_list('name', flat=True)

    auction_type = ContentType.objects.get_for_model(auction_order)
    auction_attaches = Attach.objects.filter(content_type__pk=auction_type.id, object_id=auction_order.id)

    context = {"auction_order": auction_order,
               "auction_categories": auction_categories,
               "auction_attaches": auction_attaches}
    return render(request, 'eworld/single_auction.html', context)