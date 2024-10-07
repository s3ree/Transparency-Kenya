from django.core.management.base import BaseCommand
from core.models import CountySpending
from core.scraper import get_county_spending_data 

class Command(BaseCommand):
    help = 'Fetches the latest county spending data from the Auditor General website'

    def handle(self, *args, **kwargs):
        data = get_county_spending_data() 
        if data:
            for report in data:
               
                CountySpending.objects.update_or_create(
                    county=report['county'],
                    date=report['date'],
                    defaults={
                        'amount': report['amount'],
                        'description': report['description']
                    }
                )
            self.stdout.write(self.style.SUCCESS('Successfully updated county spending data'))
        else:
            self.stdout.write(self.style.ERROR('Failed to retrieve data'))
