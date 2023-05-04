from django.contrib import admin
from .models import Carousel

# Register your models here.
@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}