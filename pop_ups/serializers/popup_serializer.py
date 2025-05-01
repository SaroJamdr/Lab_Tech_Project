from rest_framework import serializers
from ..models import PopUp, PopUpData

class PopUpDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUpData
        fields = ['id', 'title', 'image', 'link']
        

class PopUpSerializer(serializers.ModelSerializer):
    popup_images = PopUpDataSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.DictField(), write_only=True, required=False
    )

    class Meta:
        model = PopUp
        fields = ['id', 'popup_images', 'uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        popup = PopUp.objects.create(**validated_data)
        for data in uploaded_images:
            PopUpData.objects.create(
                popup=popup,
                title=data.get('title', ''),
                image=data.get('image', None),
                link=data.get('link', '')
            )
        return popup