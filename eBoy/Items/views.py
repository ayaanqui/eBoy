from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from Items.forms import SellItemForm
from Items.models import Items

@login_required
def sell(request):
    if request.method == 'POST':
        form = SellItemForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            item = Items(
                title = form.cleaned_data['title'],
                image = form.cleaned_data['image'],
                description = form.cleaned_data['description'],
                slug = slugify(form.cleaned_data['title']),
                price = form.cleaned_data['price'],
                user = request.user
            )
            item.save()
            messages.success(request, 'Awesome! Your item was added to the listing')
            return redirect('home')
        else:
            messages.error(request, 'Oops! Looks like something went wrong. Please try again')
    else:
        form = SellItemForm()

    context = {
        'page': 'sell',
        'title': 'Sell items and make money!',
        'form': form
    }
    return render(request, 'Items/sell.html', context=context)

def viewItem(request, id, slug):
    item = Items.objects.filter(id=id, slug=slug).first()
    if item:
        context = {
            'page': 'view-item',
            'title': item.title,
            'item': item
        }
        return render(request, 'Items/view-item.html', context=context)