from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message= models.TextField()
    phone= models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name