from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Attach(models.Model):
    # file = models.FileField()
    file = models.CharField(max_length=10, default='hello!')
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=10)
    content_object = GenericForeignKey()