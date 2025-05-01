from rest_framework import serializers
from ..models import Gallery, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']

class GallerySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    class Meta:
        model = Gallery
        fields = ['id', 'updated_date', 'image_link', 'images', 'uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        gallery = Gallery.objects.create(**validated_data)
        for image_file in uploaded_images:
            Image.objects.create(gallery=gallery, image=image_file)
        return gallery
