from rest_framework import serializers
from ..models import Service
from categories.models import Category
from categories.serializers.categories_serializer import CategorySerializer, SubCategorySerializer


class ServiceSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    category_name = CategorySerializer(many=True, read_only=True, source='category')
    sub_category= SubCategorySerializer(many= True, read_only= True)
        
    class Meta:
        model = Service
        fields = ('name', 'description', 'price', 'category', 'category_name','sub_category' )

    def validate(self, attrs):
        categories = attrs.get('category', [])
        sub_categories = attrs.get('sub_category', [])

        invalid_subs = [
            sub for sub in sub_categories
            if sub.parent not in categories
        ]

        if invalid_subs:
            raise serializers.ValidationError({
                "sub_category": "One or more sub-categories do not belong to the selected categories."
            })

        return attrs