"""eBoy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews
from Users import views as userViews
from Items import views as itemViews
# Media imports
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('Home.urls')),
    path('login/', authViews.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('register/', userViews.register, name='register'),
    path('sell/', itemViews.sell, name='sell'),
    path('cart/', include('Cart.urls')),
    path('items/', include('Items.urls')),
    path('search/', include('Search.urls')),
    path('admin/', admin.site.urls)
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)