from django.db import models

# Create your models here.
class Homepage(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    homepage_url = models.CharField(max_length=200, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)