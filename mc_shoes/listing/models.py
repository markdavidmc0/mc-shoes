from django.db import models


class Shoe(models.Model):
    """Shoe object database definition."""

    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    size = models.IntegerField(choices=[(i, i) for i in range(11)])
    photo = models.ImageField(upload_to='shoes')
