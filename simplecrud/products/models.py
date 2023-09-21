from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=244, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.product_name
