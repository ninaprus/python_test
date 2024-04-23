import csv
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Load data from CSV file to database'

    def handle(self, *args, **kwargs):
        products_csv_file = 'products/management/commands/products.csv'

        with open(products_csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Product.objects.create(
                    title=row['Title'],
                    asin=row['Asin'],
                )
        self.stdout.write(self.style.SUCCESS('Product data loaded successfully'))
