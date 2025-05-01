from django.db import models
from services.models import Service

class Appointment(models.Model):
    payment_choices= [
        ('online', 'online'),
        ('ofline', 'ofline')
    ]

    gender_choices= [('male', 'Male'), ('female', 'Female'), ('other', 'Other')]

    name= models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)
    services= models.ManyToManyField(Service, related_name='appointments_services')
    address= models.CharField(max_length=255)
    gender = models.CharField(choices=gender_choices, max_length=10)
    appointment_date = models.DateField()
    payment_method= models.CharField(choices=payment_choices, default='ofline')
    message= models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def total_price(self):
        return sum(service.price for service in self.services.all())