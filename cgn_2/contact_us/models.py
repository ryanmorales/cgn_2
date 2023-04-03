from django.db import models

# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=250, db_index=True)
    organization = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField(max_length=1200)
    
    def __str__(self):
        return self.email

