from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import CartItem
from products.models import Product
from django.urls import reverse_lazy


@login_required(login_url=reverse_lazy('signup'))
def cart(request):
    cart = CartItem.objects.filter(user=request.user)
    total = 0
    for item in cart:
        total += (item.price*item.quantity)
    return render(request, 'cart.html', {'cartItems': cart, 'total': total})


@login_required(login_url=reverse_lazy('signup'))
def checkout(request):
    return render(request, 'checkout.html')


@login_required(login_url=reverse_lazy('signup'))
def delivery(request):
    return render(request, 'delivery.html')


@login_required(login_url=reverse_lazy('signup'))
def create(request):
    getProduct = Product.objects.get(id=request.POST['product_id'])

    def alreadyExists(x):
        if x.user == request.user and x.product == getProduct:
            return True
        else:
            return False

    if request.method == 'POST':
        if request.POST['user'] and request.POST['product_id']:
            try:
                cartItem = list(filter(alreadyExists, CartItem.objects.all()))[0]
                cartItem.quantity += 1
                cartItem.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            except IndexError:
                cartItem = CartItem()
                cartItem.user = request.user
                cartItem.product = getProduct
                cartItem.price = cartItem.product.price
                cartItem.quantity += 1
                cartItem.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url=reverse_lazy('signup'))
def delete(request):
    def alreadyExists(x):
        if x.user == request.user and x.product == Product.objects.get(id=request.POST['product_id']):
            return True
        else:
            return False

    if request.method == "POST":
        try:
            list(filter(alreadyExists, CartItem.objects.all()))[0].delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        except IndexError:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url=reverse_lazy('signup'))
def deleteOne(request):
    if request.POST['user'] and request.POST['product_id']:
        def alreadyExists(x):
            if x.user == request.user and x.product == Product.objects.get(id=request.POST['product_id']):
                return True
            else:
                return False

        if request.method == 'POST':
            try:
                cartItem = list(filter(alreadyExists, CartItem.objects.all()))[0]
                if cartItem.quantity > 1:
                    cartItem.quantity -= 1
                    cartItem.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                else:
                    list(filter(alreadyExists, CartItem.objects.all()))[0].delete()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

            except (IndexError):
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
