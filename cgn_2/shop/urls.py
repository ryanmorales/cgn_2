from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('shop/category/<slug:category_slug>/', views.get_category_products, name='category_products'),
    path('get_brand_products/', views.get_brand_products, name='get_brand_products'),
    path('get_all_brands/', views.get_all_brands, name='get_all_brands'),
    #path('shop/brand/', views.get_brand_products, name='brands'),
]