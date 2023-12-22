# makeing cart.py globally available

# add this in templates dic in settings.py  'cart.context_processors.cart'

from .cart import Cart



def cart(request):
    return {'cart': Cart(request)}