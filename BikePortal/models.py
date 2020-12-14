from django.db import models
from django.utils import timezone

class Ticket(models.Model):

    title = models.CharField(default='task title', max_length=200)
    desc = models.TextField(default='task to do')
    date = models.DateTimeField(default=timezone.now)
    bike_name = models.CharField(default='bike not selected',max_length=50)
    priority = models.IntegerField(default=2)
    done = models.BooleanField(default=0)

    def __str__(self):
        return self.title