from rest_framework import serializers
from .models import Product, Image


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'is_published', 'category', 'price', 'description', 'create_at', 'updated_at',
            'options', 'images_path'
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id', 'product', 'image'
        ]
