from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="%(app_label)s_%(class)s_related")
    phone_number = models.CharField(max_length=15, null=True)
    reg_datetime = models.DateTimeField(auto_now_add=True)
    is_banned = models.BooleanField(default=False)
    cities = models.ManyToManyField(City)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s profile' % self.user.email


class Client(UserProfile):
    activity_index = models.FloatField(default=0.0)

    def __unicode__(self):
        return u'%s client profile' % self.user.email


class EventManager(UserProfile):
    INDIVIDUAL_PERSON = 'INDIVIDUAL'
    LEGAL_PERSON = 'LEGAL'
    LEGAL_STATUSES = ((LEGAL_PERSON, 'Legal person'), (INDIVIDUAL_PERSON, 'Individual person'))

    legal_status = models.CharField(choices=LEGAL_STATUSES, max_length=10)
    activity_index = models.FloatField(default=0.0)

    def __unicode__(self):
        return u'%s event manager profile' % self.user.email