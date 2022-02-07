from django.db import models
from django.contrib.auth.models import User


class FavoriteItem(models.Model):
    item = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
