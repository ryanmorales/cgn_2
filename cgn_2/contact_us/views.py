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
        phone_number = request.POST.get('phone_number')

        Contact.objects.create(name=name, organization=organization, email=email, phone_number=phone_number, message=message)

        send_mail('Inquiry received', 
                  'Hi! ' + '\n\n\n' 
                  + 'Thank you for reaching out with us.  We have received your contact number and email address.  ' 
                  + '\n\n' 
                  + 'Rest assured that this data will be confidential.  We will get back to you the soonest we can.' 
                  + '\n\n\n'
                  + 'Regards,'
                  + '\n'
                  + 'CGN Admin'
                  + '\n\n', settings.EMAIL_HOST_USER, [email], fail_silently=False,)

    inquire_success = True
    response = JsonResponse({'success': inquire_success})

    return response

def contact_success(request):

    return render(request, 'contact_us/contact_success.html')


def contact_failed(request):

    return render(request, 'contact_us/contact_failed.html')
