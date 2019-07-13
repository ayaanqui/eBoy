from django.urls import path
from Cart import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('delete/<int:itemId>', views.deleteCartItem, name='delete-cart-item'),
    path('<int:itemId>/<int:quantity>/', views.addToCart, name='add-to-cart'),
    path('count/', views.getCartItemsCount, name='cart-count')
]
