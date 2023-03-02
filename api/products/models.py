from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.FloatField(null=False)

    def __str__(self):
        return self.title
