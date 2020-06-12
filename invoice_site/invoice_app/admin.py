from django.contrib import admin
from invoice_app.models import InvoiceHome,InvoiceInfo

# Register your models here.
admin.site.register(InvoiceHome)
admin.site.register(InvoiceInfo)