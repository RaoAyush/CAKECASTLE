from django.shortcuts import render, get_object_or_404
from .models import Product , Category

def home(request):
    products=Product.objects.filter(is_available=True)
    return render(request, 'bakery/home.html',{'products': products})
  
def about(request):
    return render(request, 'bakery/about.html')

def contact(request):
    return render(request, 'bakery/contact.html')

def menu(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        products = Product.objects.filter(is_available=True, category__slug=selected_category)
    else:
        products = Product.objects.filter(is_available=True)

    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
    }
    return render(request, 'bakery/menu.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)
    return render(request, 'bakery/product_detail.html', {'product': product})