from django.db import models
from django.contrib.auth.models import AbstractUser
from eworld.utils import generate_filename
from random import randint
from django.conf import settings


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name


class UserProfile(AbstractUser):
    def get_upload_avatar_filename(self, filename):
        return "avatars/%s/%s/" % (str(randint(1, settings.COUNT_FOLDERS)),
                                   str(randint(1, settings.COUNT_FOLDERS))) + generate_filename(filename)

    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_banned = models.BooleanField(default=False)
    cities = models.ManyToManyField(City)
    about_me = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to=get_upload_avatar_filename)

    @property
    def is_client(self):
        try:
            return self.client is not None
        except Client.DoesNotExist:
            return False

    @property
    def is_event_manager(self):
        try:
            return self.event_manager is not None
        except EventManager.DoesNotExist:
            return False

    def save(self, *args, **kwargs):
        """ delete old avatar when replacing by updating the file """
        try:
            this = UserProfile.objects.get(id=self.id)
            if this.avatar != self.avatar:
                this.avatar.delete(save=False)
        except UserProfile.DoesNotExist:
            pass  # When new photo then we do nothing, normal case
        super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.username


class Client(models.Model):
    user = models.OneToOneField(UserProfile)
    activity_index = models.FloatField(default=0.0)

    def __unicode__(self):
        return u'Client %s' % self.user


class EventManager(models.Model):
    INDIVIDUAL_PERSON = 'INDIVIDUAL'
    LEGAL_PERSON = 'LEGAL'
    LEGAL_STATUSES = ((LEGAL_PERSON, 'Legal person'), (INDIVIDUAL_PERSON, 'Individual person'))
    legal_status = models.CharField(choices=LEGAL_STATUSES, max_length=10)

    user = models.OneToOneField(UserProfile, related_name='event_manager')
    activity_index = models.FloatField(default=0.0)

    def __unicode__(self):
        return u'Event manager %s' % self.user


class Message(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='outgoing_messages_set')
    receiver = models.ForeignKey(UserProfile, related_name='incoming_messages_set')
    theme = models.CharField(max_length=150, null=True, blank=True)
    text = models.TextField()
    is_read = models.BooleanField(default=False)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('sender', 'receiver'),)

    def __unicode__(self):
        return self.theme

