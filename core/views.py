from django.shortcuts import render ,redirect
from django.contrib.auth import login , logout
from products.models import Product ,Category
from django.db.models import Q
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_page(request):
    products = Product.objects.all()[0:8]

    ctx = {
        'products': products
    }
    return render(request, 'core/homepage.html',ctx)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    ctx = {
        'form':form
        }
    return render(request, 'core/signup.html', ctx)


@login_required
def my_account(request):

    return render(request, 'core/myaccount.html')

@login_required
def edit_account(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username =  request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        return redirect('account')

    return render(request, 'core/editaccount.html')

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    active_category = request.GET.get('category', '') # default is emty/ ''

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('q','')
    if query:
        products = products.filter(
            Q(name__icontains = query)|  
            Q(slug__icontains = query)|  
            Q(description__icontains = query)  
            )

    ctx = {
        'products': products,
        'categories': categories,
        'active_category': active_category,
    }
    return render(request, 'core/shop.html',ctx)
