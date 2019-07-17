from django.urls import path
from Search.views import Search

urlpatterns = [
    path('<str:input>/', Search.as_view(), name='search')
]
