from django.conf import settings
from django.db import models
from django.utils import timezone


class NetFlowPacket(models.Model):

    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_line = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id
