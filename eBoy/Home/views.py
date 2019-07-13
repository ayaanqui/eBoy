from django.shortcuts import render
from Items.models import Items
from Cart.models import Cart

# Create your views here.
def home(request):
    items = Items.objects.all().order_by('-date')

    context = {
        'page': 'home',
        'title': 'Home',
        'items': items
    }
    return render(request, 'Home/home.html', context=context)