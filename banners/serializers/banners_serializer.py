from rest_framework import serializers
from ..models import Banner
import os

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('image', 'image_link', 'video', 'video_link', 'description')

    def validate(self, data):
        if (data.get('image') and data.get('video')) or (not data.get('image') and not data.get('video')):
            raise serializers.ValidationError('You must provide either an image or a video, but not both.')
        return data
    

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)

        if self.video and os.path.isfile(self.video.path):
            os.remove(self.video.path)

        super().delete(*args, **kwargs)