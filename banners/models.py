from django.db import models
import os

class Banner(models.Model):
    image= models.ImageField(upload_to='banner/', null=True, blank=True)
    image_link= models.URLField(null= True, blank=True)
    video= models.FileField(upload_to='banner/', null=True, blank=True)
    video_link= models.URLField(blank=True, null=True)
    description= models.TextField(null= True, blank=True)

    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Banner {self.id}"
    
    def delete(self, *args, **kwargs):
        # Delete files if they exist and path is valid
        if self.image and hasattr(self.image, 'path') and os.path.isfile(self.image.path):
            os.remove(self.image.path)

        if self.video and hasattr(self.video, 'path') and os.path.isfile(self.video.path):
            os.remove(self.video.path)

        super().delete(*args, **kwargs)