from django.urls import path 
from django.contrib.auth import views
from .views import home_page, signup ,shop , my_account , edit_account

from products.views import product

urlpatterns = [
    path('', home_page, name='home'),
    path('shop/', shop, name='shop'),
    path('signup/', signup, name='signup'),
    path('my_account/', my_account, name='account'),
    path('edit_account/', edit_account, name='edit-account'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),

    path('shop/<slug:slug>/',product, name='product'),
]
