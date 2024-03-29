from django.urls import path
from .views import (
    HomeView,
    CheckoutView,
    ItemDetailView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView
)

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart' )
]