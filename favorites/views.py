from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import FavoriteItem
from products.models import Product
from django.urls import reverse_lazy


@login_required(login_url=reverse_lazy('signup'))
def favorites(request):
    favItems = list(FavoriteItem.objects.filter(user=request.user))
    return render(request, 'favorites.html', {'favItems':favItems})


@login_required(login_url=reverse_lazy('signup'))
def toggleFav(request):
    def alreadyExists(x):
        if x.user == request.user and x.item == Product.objects.get(id=request.POST['product_id']):
            return True
        else:
            return False
    if request.method == 'POST':
        if request.POST['user'] and request.POST['product_id']:
            try:
                list(filter(alreadyExists, FavoriteItem.objects.all()))[0].delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            except IndexError:
                favItem = FavoriteItem()
                favItem.user = request.user
                favItem.item = Product.objects.get(id=request.POST['product_id'])
                favItem.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
