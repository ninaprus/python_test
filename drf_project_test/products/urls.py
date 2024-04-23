from django.urls import path
from .views import ProductDetail

urlpatterns = [
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]