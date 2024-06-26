from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'review_text']


class NewReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'review_text']