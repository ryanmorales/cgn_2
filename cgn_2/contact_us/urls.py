from django.urls import path
from . import views

urlpatterns = [

    path('', views.contact_us, name='contact_us'),
    path('submit_inquiry', views.submit_inquiry, name='submit_inquiry'),
    path('contact_success', views.contact_success, name='contact_success'),
    path('contact_failed', views.contact_failed, name='contact_failed')

]