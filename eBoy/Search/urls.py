from django.urls import path
from Search.views import search

urlpatterns = [
    path('<str:input>/', search, name='search')
]
