from django.db import models
from profiles.models import City, UserProfile


class BaseEvent(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(blank=True, null=True)
    city = models.ForeignKey(City)
    price = models.FloatField(default=0)
    description = models.TextField()
    requirements = models.TextField()
    order_views = models.ManyToManyField(UserProfile, null=True, blank=True)

    class Meta:
        abstract = True


class Order(BaseEvent):
    FINDING_MANAGER = 'FINDING_MANAGER'
    FOUND_MANAGER = 'FOUND_MANAGER'
    IN_WORK = 'IN_WORK'
    COMPLETED = 'COMPLETED'
    ORDER_STATUSES = ((FINDING_MANAGER, 'Finding event manager'), (FOUND_MANAGER, 'Event manager found'),
                      (IN_WORK, 'Order in progress'), (COMPLETED, 'Order completed'))

    order_state = models.CharField(choices=ORDER_STATUSES, max_length=15)


class AuctionOrder(BaseEvent):
    pass