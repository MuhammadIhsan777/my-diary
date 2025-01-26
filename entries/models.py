from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"