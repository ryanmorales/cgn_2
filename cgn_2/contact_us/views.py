from django.shortcuts import render
from . models import Contact

from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse


# Create your views here.

def contact_us(request):

    return render(request, 'contact_us/contact_us.html')

def submit_inquiry(request):

    #if request.method == 'POST':
    if request.POST.get('action') == 'post':

        name = request.POST.get('name')
        organization = request.POST.get('organization')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(name=name, organization=organization, email=email, message=message)

        #send_mail('Order received', 'Hi! ' + '\n\n' + 'Thank you for reaching out with us' + '\n\n' + 
        #'We will get back that soonest we can.' + '\n\n', settings.EMAIL_HOST_USER, [email], fail_silently=False,)

    inquire_success = True
    response = JsonResponse({'success': inquire_success})

    return response

def contact_success(request):

    return render(request, 'contact_us/contact_success.html')


def contact_failed(request):

    return render(request, 'contact_us/contact_failed.html')
