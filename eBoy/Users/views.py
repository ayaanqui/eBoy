from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from Users.forms import UserRegisterForm

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Awesome! Account created. You can now login')
                return redirect('login')
            else:
                messages.error(request, 'Oops! Something went wrong. Please try submitting the form again')
        else:
            form = UserRegisterForm()

        context = {
            'page': 'register',
            'title': 'Make an account today',
            'form': form
        }
        return render(request, 'Users/register.html', context=context)
    else:
        return redirect('home')