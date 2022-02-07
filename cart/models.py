from django.db import models
from django.contrib.auth.models import User


class CartItem(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def calcPrice(self):
        return str(self.price) + " x " + str(self.quantity) + ", " + str(self.price * self.quantity) + "$"
