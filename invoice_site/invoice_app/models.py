from django.db import models

# Create your models here.

class Invoice(models.Model):
    invoice_number = models.CharField(primary_key=True,max_length=256)
    invoice_name = models.CharField(max_length=256, null=False)
    invoice_date = models.DateField()

    def __str__(self):
        return f'Name:{self.invoice_name}'
