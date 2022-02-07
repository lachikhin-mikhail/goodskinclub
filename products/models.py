from django.db import models
from stdimage.models import StdImageField


class Product(models.Model):
    class Category(models.TextChoices):
        FACE = 'f', "FACE"
        HAIR = 'h', "HAIR"
        BODY = 'b', 'BODY'

    class SkinType(models.TextChoices):
        NONE = 'n', "NONE"
        OILY = 'o', 'OILY'
        DRY = 'd', 'DRY'
        COMB = 'c', 'COMBINATION'

    title = models.CharField(max_length=255)
    description = models.TextField()
    volume = models.IntegerField()
    price = models.IntegerField()
    ingridients = models.TextField()
    image = StdImageField(upload_to='images/', variations={"big":{"width": 668, "height": 741, "crop": True},"small":{"width": 292, "height": 292, "crop": True}})
    category = models.CharField(max_length=2, choices=Category.choices)
    skinType = models.CharField(max_length=2, choices=SkinType.choices)


    def __str__(self):
        return self.title

    def shortTitle(self):
        if len(self.title) > 30:
            return (self.title[:20]+"...")
        else:
            return self.title
