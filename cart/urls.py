from django.urls import path
from cart.views import add_to_cart ,cart_view ,checkout_view ,hx_menu_cart ,update_cart , hx_cart_total ,success

urlpatterns = [
    path('',cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/',add_to_cart, name='add_to_cart'),
    path('checkout/',checkout_view, name='checkout'),
    path('update_cart/<int:product_id>/<str:action>/',update_cart, name='update-cart'),
    path('success/',success, name='success'),

    path('hx_menu_cart/',hx_menu_cart, name='hx_menu_cart'),
    path('hx_cart_total/',hx_cart_total, name='hx_cart_total'),


]
