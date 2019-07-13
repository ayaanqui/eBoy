from django.urls import path
from Items.views import viewItem

urlpatterns = [
    path('<int:id>/<str:slug>/', viewItem, name='view-item')
]
