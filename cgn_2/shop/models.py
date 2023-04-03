from django.db import models

from django.urls import reverse
from django import forms

# Create your models here.

class Carousel(models.Model):

    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'carousels'

    def __str__(self):
        return self.name
        

class Category(models.Model):

    category_name = models.CharField(max_length=250, db_index=True)
    category_slug = models.SlugField(max_length=250)
    category_description = models.TextField(max_length=1200)
    category_active = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category-info', args=[self.category_slug])


class Brand(models.Model):

    brand_name = models.CharField(max_length=250, db_index=True)
    brand_slug = models.SlugField(max_length=250)
    brand_description = models.TextField(max_length=1200)
    brand_active = models.BooleanField(default=False)
    brand_image = models.ImageField(upload_to='images/brands/')

    brand_category = models.ForeignKey(Category, related_name='brand_category', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand_name
    
    def get_absolute_url(self):
        return reverse('brand-info', args=[self.brand_slug])


class Product(models.Model):

    product_name = models.CharField(max_length=250, db_index=True)
    product_slug = models.SlugField(max_length=250)
    product_description = models.TextField(max_length=1200)
    product_active = models.BooleanField(default=False)
    product_image = models.ImageField(upload_to='images/products/')

    product_category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE, null=True)
    product_brand = models.ForeignKey(Brand, related_name='product_brand', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('product-info', args=[self.product_slug])












    











