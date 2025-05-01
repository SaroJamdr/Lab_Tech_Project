from django.db import models
from categories .models import Category

class Service(models.Model):
    name = models.CharField(max_length=100)
    category= models.ManyToManyField(Category, related_name='service_categories')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags= models.CharField(max_length=100)
    description = models.TextField()
    feature_image = models.ImageField(upload_to='services')
    other_images= models.ImageField(upload_to='services', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name