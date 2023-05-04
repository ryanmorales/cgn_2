from django.db import models

# Create your models here.

class Carousel(models.Model):

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'shop_carousel'

    def __str__(self):
        return self.name