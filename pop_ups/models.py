from django.db import models

class PopUp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PopUp {self.id}"

class PopUpData(models.Model):
    popup = models.ForeignKey(PopUp, related_name='popup_images', on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    image= models.ImageField(upload_to='pop_up/')
    link= models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
