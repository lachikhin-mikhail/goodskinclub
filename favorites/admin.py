from django.contrib import admin

# Register your models here.
from .models import FavoriteItem

admin.site.register(FavoriteItem)
