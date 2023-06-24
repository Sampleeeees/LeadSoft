from datetime import datetime

from django.db import models

# Create your models here.
class Visit(models.Model):
    user_id = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user_id