from django.shortcuts import render ,get_object_or_404, redirect
from .models import Product ,Review

# Create your views here.

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')
        
        if content:
            review = Review.objects.filter(created_by = request.user, product= product)

            if review.count() > 0 :
                review =review.first()
                review.ratings =rating
                review.content = content
                review.save()

            else:
                review = Review.objects.create(
                    product = product,
                    content = content,
                    ratings = rating,
                    created_by = request.user,
                )


            return redirect('product', slug=slug)

    ctx = {
        'product':product
    }
    return render(request, 'products/product.html' ,ctx)
