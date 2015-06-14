from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from random import randint
from django.conf import settings
from eworld.utils import generate_filename
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


def get_upload_file_path(instance, filename):
    return "attaches/%s/%s/" % (str(randint(1, settings.COUNT_FOLDERS)),
                                str(randint(1, settings.COUNT_FOLDERS))) + generate_filename(filename)


class Attach(models.Model):
    file = models.FileField(upload_to=get_upload_file_path)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=10)
    content_object = GenericForeignKey()

    def save(self, *args, **kwargs):
        """ delete old file when replacing by updating the file """
        try:
            this = Attach.objects.get(id=self.id)
            if this.file != self.file:
                this.file.delete(save=False)
        except Attach.DoesNotExist:
            pass  # When new photo then we do nothing, normal case
        super(Attach, self).save(*args, **kwargs)


@receiver(pre_delete, sender=Attach)
def attach_file_delete(sender, instance, **kwargs):
    """ delete image when remove object from admin panel """
    instance.file.delete(False)