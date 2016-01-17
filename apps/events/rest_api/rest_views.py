__author__ = 'PerminovMA@live.ru'

from events.rest_api.serializers import AuctionOrderSerializer, CategorySerializer, OrderSerializer, BetSerializer, \
    CommentSerializer
from events.models import AuctionOrder, Category, Order, Bet, OrderComment
from rest_framework import viewsets
import datetime, json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from django.http import HttpResponse
from profiles.models import EventManager
from rest_framework.permissions import IsAuthenticated
from profiles.rest_api.permissions import IsEventManagers


class AuctionOrderView(viewsets.ModelViewSet):
    serializer_class = AuctionOrderSerializer
    permission_classes = (IsAuthenticated,)

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

    @detail_route(methods=['get'])
    def best_bets(self, request, pk=None):
        auction = get_object_or_404(AuctionOrder, pk=pk)
        bets_queryset = auction.get_best_bet(5)
        serializer = BetSerializer(bets_queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def comments(self, request, pk=None):
        auction = get_object_or_404(AuctionOrder, pk=pk)
        serializer = CommentSerializer(auction.comments, many=True)
        return Response(serializer.data)

    @detail_route(methods=['put'], permission_classes=[IsAuthenticated, IsEventManagers])
    def to_bet(self, request, pk=None):
        new_amount = request.data.get('amount')
        if new_amount is None:
            return HttpResponse(json.dumps({"result": "fail", "message": "'amount' not found"}))
        print new_amount

        auction = get_object_or_404(AuctionOrder, pk=pk)
        if auction.status != AuctionOrder.AUCTION_IN_PROCESS:
            return HttpResponse(json.dumps({"result": "fail", "message": "Auction closed"}))

        # if min_price is None then min_price = 50% of start_price
        min_price = auction.min_price if auction.min_price else auction.start_price / 2
        if new_amount < min_price:
            return HttpResponse(json.dumps({"result": "fail", "message": "New amount less than min price"}))

        if new_amount == min_price:
            new_bet = Bet.objects.create(auction=auction, amount=new_amount, owner=request.user.event_manager)
            serializer = BetSerializer(new_bet)
            auction.status = AuctionOrder.MANAGER_SELECTING
            auction.save(update_fields=['status'])
            return HttpResponse(json.dumps({"result": "success", "message": "Bet created", "new_bet": serializer.data}))

        best_bet_list = auction.get_best_bet(1)
        if best_bet_list:
            best_bet = best_bet_list[0]
            if new_amount > best_bet.amount:
                return HttpResponse(json.dumps({"result": "fail", "message": "New amount more than best bet amount"}))

        new_bet = Bet.objects.create(auction=auction, amount=new_amount, owner=request.user.event_manager)
        serializer = BetSerializer(new_bet)

        return HttpResponse(json.dumps({"result": "success", "message": "Bet created", "new_bet": serializer.data}))

    @detail_route(methods=['put'], permission_classes=[IsAuthenticated, IsEventManagers])
    def make_comment(self, request, pk=None):
        auction = get_object_or_404(AuctionOrder, pk=pk)
        if auction.status != AuctionOrder.AUCTION_IN_PROCESS:
            return HttpResponse(json.dumps({"result": "fail", "message": "Auction closed"}))

        text = request.GET.get('text')
        answer_to = request.GET.get('answer_to')  # if this message is the answer, it is parameter - other comment ID

        if answer_to:
            answer_to = get_object_or_404(OrderComment, pk=answer_to)

        auction.comments.add(OrderComment.objects.create(owner=request.user, text=text, answer_to=answer_to))

        return HttpResponse(answer_to)


class OrderView(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)
