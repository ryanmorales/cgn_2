from django.urls import path
from . import views

urlpatterns = [

    path('', views.shop, name='shop'),
    path('all_products/', views.get_all_products, name='all_products'),
    path('all_brands/', views.get_all_brands, name='all_brands'),

    path('product/<int:pk>', views.product_detail, name='product_detail'),
    #path('shop/category/<slug:category_slug>/', views.get_category_products, name='category_products'),
    #path('get_brand_products/<str:this_brand>/', views.get_brand_products, name='get_brand_products'),
    #path('', views.get_brand_products, name='get_brand_products'),
    #path('get_all_brands/', views.get_all_brands, name='get_all_brands'),
    #path('submit_brand_data/<str:this_brand>/', views.submit_brand_data, name='submit_brand_data'),
]