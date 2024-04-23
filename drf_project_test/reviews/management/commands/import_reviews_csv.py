import csv
from django.core.management.base import BaseCommand
from reviews.models import Review
from products.models import Product


class Command(BaseCommand):
    help = 'Load data from CSV file to database'

    def handle(self, *args, **kwargs):
        reviews_csv_file = 'reviews/management/commands/reviews.csv'

        with open(reviews_csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    product = Product.objects.get(asin=row['Asin'])
                except Product.DoesNotExist:
                    # self.stdout.write(f"{row['Asin']} DoesNotExist")
                    continue
            
                Review.objects.create(
                    title=row['Title'],
                    product=product,
                    review_text=row['Review']
                )
        self.stdout.write(self.style.SUCCESS('Review data loaded successfully'))