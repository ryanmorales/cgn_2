from django.db import models

from django.urls import reverse
from ckeditor.fields import RichTextField


class About(models.Model):

    intro = RichTextField()
    vision = RichTextField()
    mission = RichTextField()
    product_range = RichTextField()
    company_details = RichTextField()

    def __str__(self):
        return self.intro