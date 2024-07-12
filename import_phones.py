import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                phone, created = Phone.objects.get_or_create(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'] == 'True'
                )
                self.stdout.write(self.style.SUCCESS(f'{"Created" if created else "Updated"} phone: {phone.name}'))