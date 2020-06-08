from invoice_app.models import Invoice
from django import forms

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number','invoice_name','invoice_date']
