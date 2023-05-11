from django.shortcuts import render
from . models import Category, Brand, Product
from django.shortcuts import get_object_or_404

from django.conf import settings
from django.core.mail import send_mail

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
    

def get_a_quote(request, pk):

    product = get_object_or_404(Product, pk=pk)
    category = request.GET.get('category')
    brand = request.GET.get('brand')

    context = {
            'product': product,
            'active_category' : category,
            'active_brand' : brand,
    }

    return render(request, 'shop/get_a_quote.html', context=context)


def send_a_quote(request):
    
    if request.POST.get('action') == 'post':

        name = request.POST.get('name')
        organization = request.POST.get('organization')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone_number = request.POST.get('phone_number')
        product_name = request.POST.get('product_name')
        product_qty = request.POST.get('qty')

        send_mail('Request a quote received', 
                  'Hi! ' + name + '\n\n\n' 
                  + 'You requested ' + product_qty + ' of ' + product_name + ' We will contact your number ' + phone_number 
                  + ' as soon as we can.'
                  + '\n\n' 
                  + 'Rest assured that this data will be confidential.  We will get back to you the soonest we can.' 
                  + '\n\n\n'
                  + 'Regards,'
                  + '\n'
                  + 'CGN Admin'
                  + '\n\n', settings.EMAIL_HOST_USER, [email, settings.EMAIL_HOST_USER], fail_silently=False,)

    send_a_quote_success = True
    response = JsonResponse({'success': send_a_quote_success})

    return response


def send_a_quote_success(request):
    
    return render(request, 'shop/send_a_quote_success.html')


def send_a_quote_failed(request):
    
    return render(request, 'shop/send_a_quote_failed.html')