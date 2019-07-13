from django.urls import path
from Home import views as homeViews

urlpatterns = [
    path('', homeViews.home, name='home')
]
