from django.shortcuts import render
from . models import Carousel
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):

    carousel_items = Carousel.objects.filter(active=True)
    context = {'carousel_items': carousel_items}
    return render(request, 'home/home.html', context=context)


