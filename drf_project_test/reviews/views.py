
from rest_framework import generics

from products.models import Product
from reviews.serializers import NewReviewSerializer


class NewReviewCreate(generics.CreateAPIView):
    serializer_class = NewReviewSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(pk=product_id)
        serializer.save(product=product)
