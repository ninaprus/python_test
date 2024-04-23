from rest_framework import generics, pagination
from products.models import Product
from products.serializers import ProductSerializer
from reviews.serializers import ReviewSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        reviews = instance.reviews.all()
        paginator = CustomPagination()
        page = paginator.paginate_queryset(reviews, request)

        serializer = self.get_serializer(instance)
        data = serializer.data

        if page is not None:
            review_serializer = ReviewSerializer(page, many=True)
            data['reviews'] = paginator.get_paginated_response(review_serializer.data).data
        else:
            review_serializer = ReviewSerializer(reviews, many=True)
            data['reviews'] = review_serializer.data

        return Response(data)
