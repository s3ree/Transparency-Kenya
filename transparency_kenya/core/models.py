from django.db import models

class CountySpending(models.Model):
    county = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.county} - {self.amount}"

