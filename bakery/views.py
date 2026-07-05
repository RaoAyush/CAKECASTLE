from django.shortcuts import render
from .models import Product

def home(request):
    products=Product.objects.filter(is_available=True)
    return render(request, 'bakery/home.html',{'products': products})

# Create your views here.
