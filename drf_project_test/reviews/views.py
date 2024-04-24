
from rest_framework import generics
from rest_framework.exceptions import NotFound

from products.models import Product
from reviews.serializers import NewReviewSerializer


class NewReviewCreate(generics.CreateAPIView):
    serializer_class = NewReviewSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise NotFound("Product does not exist.")
        serializer.save(product=product)
