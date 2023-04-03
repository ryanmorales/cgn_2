from django.shortcuts import render
from . models import Carousel, Category, Brand, Product
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from django.core.serializers import serialize
import json


# Create your views here.


def home(request):

    carousel_items = Carousel.objects.filter(active=True)
    context = {'carousel_items': carousel_items}
    print(context)
    return render(request, 'shop/home.html', context=context)


def shop(request):

    all_brands = Brand.objects.filter(brand_active=True)
    context = {'all_brands': all_brands}
    return render(request, 'shop/shop.html', context=context)


def categories(request):

    all_categories = Category.objects.all()
    return {'all_categories': all_categories}


def listing_categories(request, category_slug=None):

    category = get_object_or_404(Category, category_slug=category_slug)
    products = Product.objects.filter(product_category=category)

    return render(request)


def category_brands(request, category_slug=None):

    categories = Category.objects.filter(category_active=True)
    category_data = []
    for category in categories:
        brands = Brand.objects.filter(brand_active=True, brand_category=category)
        brand_data = []
        for brand in brands:
            brand_data.append({
                'brand_name':brand.brand_name 
            })
        category_data.append({
            'category':category.category_name,
            'brands':brand_data,
            'count':len(brand_data)
        })

    return {'accordion_data':category_data}
 

def get_brand_products(request):

    if request.POST.get('data_request') == 'brand':

        brand_slug = request.POST.get('data_content')
    
        if request.POST.get('action') == 'post':

            brand = get_object_or_404(Brand, brand_slug=brand_slug.lower())
            print(brand)     
            brand_products = Product.objects.filter(product_active=True, product_brand=brand)
            print(brand_products)

            serialized_data = serialize("json", brand_products)
            serialized_data = json.loads(serialized_data)

            response = JsonResponse({'brand_products':serialized_data}, safe=False)
            return response
    else:
        return JsonResponse({'no-data': 'No Data'})

def get_all_brands(request):

    if request.POST.get('action') == 'post':
    
        all_brands = Brand.objects.filter(brand_active=True)
        serialized_data = serialize("json", all_brands)
        serialized_data = json.loads(serialized_data)
        response = JsonResponse({'brand_products':serialized_data}, safe=False)
        return response
        #return {'all_brands':all_brands}

def get_category_products(request):
    
    pass

    
