from django.shortcuts import render
from . models import Category, Brand, Product
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator

from django.http import JsonResponse, HttpResponseRedirect
from django.core.serializers import serialize
import json

def shop(request):

    category = request.GET.get('category')
    brand = request.GET.get('brand')
    all_brands = request.GET.get('brands')
    active_category = None
    active_brand = None

    products = Product.objects.filter(product_active=True)
    context = {'products': products }    

    if category:

        products = Product.objects.filter(product_active=True, product_category__category_name=category)
        active_category = category
        
    if brand:
        
        products = Product.objects.filter(product_active=True, product_brand__brand_name=brand)
        active_brand = brand
       
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if all_brands:
        brands = Brand.objects.filter(brand_active=True)
        context = {'all_brands': brands}
    else:
        context = {
                'products': products,
                'active_category' : active_category,
                'active_brand' : active_brand,
                'page_obj' : page_obj,
        }

    return render(request, 'shop/shop.html', context=context)


def categories(request):

    all_categories = Category.objects.all()
    return {'all_categories': all_categories}


def get_all_products(request):

    print("Ryan")
    all_products = Product.objects.filter(product_active=True)
    return render(request, 'shop/shop.html', {'all_products': all_products})


def get_all_brands(request):

    all_brands = Brand.objects.filter(brand_active=True)
    return render(request, 'shop/shop.html', {'all_brands': all_brands})


def category_brands(request, category_slug=None):

    categories = Category.objects.filter(category_active=True)
    category_data = []
    for category in categories:
        brands = Brand.objects.filter(brand_active=True, brand_category=category)
        brand_data = []
        for brand in brands:

            products = Product.objects.filter(product_active=True, product_brand__brand_name=brand)
            brand_data.append({
                'brand_name':brand.brand_name, 
                'count': len(products)
            })
        category_data.append({
            'category':category.category_name,
            'brands':brand_data,
            'count':len(brand_data)
        })

    return {'accordion_data':category_data}
 

def product_detail(request, pk):
    
    product = get_object_or_404(Product, pk=pk)
    category = request.GET.get('category')
    brand = request.GET.get('brand')

    context = {
            'product': product,
            'active_category' : category,
            'active_brand' : brand,
    }

    return render(request, 'shop/product_detail.html', context=context)
    
