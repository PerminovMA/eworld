# -*- coding: utf-8 -*-

from django.db import models
from profiles.models import City, UserProfile, EventManager, Client
from django.contrib.contenttypes.fields import GenericRelation
from eworld.models import Attach
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from eworld.utils import generate_filename


def get_upload_category_icon_path(instance, filename):
    return "category_icons/" + generate_filename(filename)


class Category(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to=get_upload_category_icon_path)
    order_percent = models.DecimalField(max_digits=6, decimal_places=2)
    auction_percent = models.DecimalField(max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        """ delete old icon when replacing by updating the icon """
        try:
            this = Category.objects.get(id=self.id)
            if this.icon != self.icon:
                this.icon.delete(save=False)
        except Category.DoesNotExist:
            pass  # When new photo then we do nothing, normal case
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


@receiver(pre_delete, sender=Category)
def category_icon_deleter(sender, instance, **kwargs):
    """ delete icon when remove object from admin panel """
    instance.icon.delete(False)


class BaseOrder(models.Model):
    ORDER_COMPLETE = 'ORDER_COMPLETE'
    ORDER_IN_PROCESS = 'ORDER_IN_PROCESS'

    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Client, related_name='%(class)s_set')
    creation_datetime = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(blank=True, null=True)
    city = models.ForeignKey(City)
    description = models.TextField()
    requirements = models.TextField(null=True, blank=True)
    order_views = models.ManyToManyField(UserProfile, blank=True, related_name='%(class)s_views_set')
    categories = models.ManyToManyField(Category, blank=True, related_name='%(class)s_set')

    class Meta:
        abstract = True


class Order(BaseOrder):
    FINDING_MANAGER = 'FINDING_MANAGER'
    FOUND_MANAGER = 'FOUND_MANAGER'
    ORDER_STATUSES = ((FINDING_MANAGER, 'Finding event manager'), (FOUND_MANAGER, 'Event manager found'),
                      (BaseOrder.ORDER_IN_PROCESS, 'Order in process'), (BaseOrder.ORDER_COMPLETE, 'Order complete'))

    status = models.CharField(choices=ORDER_STATUSES, max_length=16, default=FINDING_MANAGER)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    attaches = GenericRelation(Attach, related_query_name='order', content_type_field='content_type',
                               object_id_field='object_id')

    def __unicode__(self):
        return self.name


class AuctionOrder(BaseOrder):
    AUCTION_IN_PROCESS = 'AUCTION_IN_PROCESS'
    MANAGER_SELECTING = 'MANAGER_SELECTING'
    MANAGER_SELECTED = 'MANAGER_SELECTED'
    AUCTION_STATUSES = ((AUCTION_IN_PROCESS, 'auction in process'), (MANAGER_SELECTING, 'manager_selecting'),
                        (MANAGER_SELECTED, 'manager_selected'), (BaseOrder.ORDER_IN_PROCESS, 'order_in_process'),
                        (BaseOrder.ORDER_COMPLETE, 'ORDER_COMPLETE'))

    start_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    status = models.CharField(choices=AUCTION_STATUSES, max_length=18, default=AUCTION_IN_PROCESS)
    attaches = GenericRelation(Attach, related_query_name='auction_order', content_type_field='content_type',
                               object_id_field='object_id')

    def get_best_bet(self, count=1):
        if count <= 0:
            return None
        return self.bet_set.order_by('amount')[0:count]

    def __unicode__(self):
        return self.name


class Bet(models.Model):
    auction = models.ForeignKey(AuctionOrder)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    owner = models.ForeignKey(EventManager)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s" % (self.owner, self.amount)