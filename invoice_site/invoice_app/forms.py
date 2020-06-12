from invoice_app.models import InvoiceInfo, InvoiceHome
from django import forms


class InvoiceHomeForm(forms.ModelForm):
    class Meta:
        model = InvoiceHome
        fields = ['user','uploaded_pdf']


class InvoiceInfoForm(forms.ModelForm):
    class Meta:
        model = InvoiceInfo
        fields = ['invoice_number', 'vendor_name', 'invoice_date']
