from django.urls import path
from reviews.views import NewReviewCreate

urlpatterns = [
    path('create_review/<int:product_id>/', NewReviewCreate.as_view(), name='new-review-create'),
]