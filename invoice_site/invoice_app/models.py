from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class InvoiceHome(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    uploaded_pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return f'User:{self.user}  URL:{self.uploaded_pdf}'


class InvoiceInfo(models.Model):
    invoice_pdf = models.OneToOneField(InvoiceHome, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=256)
    vendor_name = models.CharField(max_length=256, null=False)
    invoice_date = models.DateField()

    def __str__(self):
        return f'Name:{self.invoice_pdf}'
