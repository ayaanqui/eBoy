from django.shortcuts import render, redirect
from Items.models import Items
from Cart.models import Cart
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user).order_by('-id')

    context = {
        'page': 'cart',
        'title': 'Cart',
        'cart': cart
    }
    return render(request, 'Cart/cart.html', context=context)

@login_required
def addToCart(request, itemId, quantity=1):
    if request.method == 'GET':
        item = Items.objects.filter(id=itemId).first()
        if item:
            cartItem = Cart.objects.filter(item=item, user=request.user).first()
            if cartItem:
                cartItem.quantity = str(int(cartItem.quantity) + quantity)
                cartItem.save()
            else:
                cart = Cart(user=request.user, item=item, quantity=quantity)
                cart.save()
            
            return JsonResponse({
                    'message': 'Added to cart',
                    'cart': quantity
                })
        else:
            return JsonResponse({
                'message': 'Error 404 not found'
            })

@login_required
def getCartItemsCount(request):
    cartItems = Cart.objects.filter(user=request.user)
    count = 0
    for item in cartItems:
        count += int(item.quantity)

    return JsonResponse({
        'count': count
    })

@login_required
def deleteCartItem(request, itemId):
    item = Items.objects.filter(id=itemId).first()
    if item:
        cartItem = Cart.objects.filter(user=request.user, item=item).first()
        if cartItem:
            cartItem.delete()
            messages.success(request, 'Item removed from cart!')
        else:
            messages.info(request, 'Item does not exist in your cart')
    else:
        messages.info(request, 'Item does not exist')

    return redirect('cart')