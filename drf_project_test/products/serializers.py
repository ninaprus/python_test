from rest_framework import serializers
from products.models import Product
from reviews.serializers import ReviewSerializer


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'asin', 'title', 'reviews']