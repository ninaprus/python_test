from django.db import models

from django.db import models


class Product(models.Model):
    asin = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=255)
