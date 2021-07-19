from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField(max_length=100)
    is_seen = models.BooleanField(default=False)
