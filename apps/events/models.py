# -*- coding: utf-8 -*-

from django.db import models
from profiles.models import City, UserProfile, EventManager


class Category(models.Model):
    name = models.CharField(max_length=20)
    # icon_file
    order_percent = models.FloatField()
    auction_percent = models.FloatField()

    def __unicode__(self):
        return self.name


class BaseEvent(models.Model):
    ORDER_COMPLETE = 'ORDER_COMPLETE'
    ORDER_IN_PROCESS = 'ORDER_IN_PROCESS'

    name = models.CharField(max_length=50)
    owner = models.ForeignKey(UserProfile, related_name='%(class)s_set')
    creation_datetime = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(blank=True, null=True)
    city = models.ForeignKey(City)
    description = models.TextField()
    requirements = models.TextField(null=True, blank=True)
    order_views = models.ManyToManyField(UserProfile, blank=True, related_name='%(class)s_views_set')
    categories = models.ManyToManyField(Category, blank=True, related_name='%(class)s_categories_set')

    class Meta:
        abstract = True


class Order(BaseEvent):
    FINDING_MANAGER = 'FINDING_MANAGER'
    FOUND_MANAGER = 'FOUND_MANAGER'
    ORDER_STATUSES = ((FINDING_MANAGER, 'Finding event manager'), (FOUND_MANAGER, 'Event manager found'),
                      (BaseEvent.ORDER_IN_PROCESS, 'Order in process'), (BaseEvent.ORDER_COMPLETE, 'Order complete'))

    status = models.CharField(choices=ORDER_STATUSES, max_length=16)
    price = models.FloatField()

    def __unicode__(self):
        return self.name


class AuctionOrder(BaseEvent):
    AUCTION_IN_PROCESS = 'AUCTION_IN_PROCESS'
    MANAGER_SELECTING = 'MANAGER_SELECTING'
    MANAGER_SELECTED = 'MANAGER_SELECTED'
    AUCTION_STATUSES = ((AUCTION_IN_PROCESS, 'auction in process'), (MANAGER_SELECTING, 'manager_selecting'),
                        (MANAGER_SELECTED, 'manager_selected'), (BaseEvent.ORDER_IN_PROCESS, 'order_in_process'),
                        (BaseEvent.ORDER_COMPLETE, 'ORDER_COMPLETE'))

    start_price = models.FloatField()
    status = models.CharField(choices=AUCTION_STATUSES, max_length=18)


    @property
    def current_price(self):
        pass  # TODO must be implemented

    def __unicode__(self):
        return self.name


class Bet(models.Model):
    auction = models.ForeignKey(AuctionOrder)
    amount = models.FloatField()
    owner = models.ForeignKey(EventManager)

    def __unicode__(self):
        return "%s : %s" % (self.owner, self.amount)