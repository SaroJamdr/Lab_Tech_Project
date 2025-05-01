from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address= models.TextField()
    gps_location= models.CharField(max_length=255)
    is_headbranch= models.BooleanField(default=False)

    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name