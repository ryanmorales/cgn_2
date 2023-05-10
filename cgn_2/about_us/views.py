from django.shortcuts import render

from . models import About

def about_us(request):

    about = About.objects.all
    return render(request, 'about_us/about_us.html', {'about_us': about})


