from django.urls import path
from . import views

urlpatterns = [

    path('', views.shop, name='shop'),
    path('all_products/', views.get_all_products, name='all_products'),
    path('all_brands/', views.get_all_brands, name='all_brands'),

    path('product/<int:pk>', views.product_detail, name='product_detail'),
    path('get_a_quote/<int:pk>', views.get_a_quote, name='get_a_quote'),
    path('send_a_quote/', views.send_a_quote, name='send_a_quote'),
    path('send_a_quote_success', views.send_a_quote_success, name='send_a_quote_success'),
    path('send_a_quote_failed', views.send_a_quote_failed, name='send_a_quote_failed'),

    #path('shop/category/<slug:category_slug>/', views.get_category_products, name='category_products'),
    #path('get_brand_products/<str:this_brand>/', views.get_brand_products, name='get_brand_products'),
    #path('', views.get_brand_products, name='get_brand_products'),
    #path('get_all_brands/', views.get_all_brands, name='get_all_brands'),
    #path('submit_brand_data/<str:this_brand>/', views.submit_brand_data, name='submit_brand_data'),
]