from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product

def app(request):
    products = Product.objects.all()        
    return render(request, 'newApp/app.html', {'products': products})

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    
    return render(request, 'newApp/app.html', {'products': products, 'search_query': query})

def about(request):
    return render(request, 'newApp/about.html')

def contact(request):
    return render(request, 'newApp/contact.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'newApp/product_detail.html', {'product': product})

# Create your views here.
