from django.shortcuts import render
from invoice_app import forms
from django.views.generic import TemplateView,CreateView

# Create your views here.

# def users(request):
#     form = InvoiceForm()

class HomePage(TemplateView):
    template_name = 'invoice_app/invoice_page.html'


class DetailsPage(CreateView):
    form_class = forms.InvoiceForm
    template_name = 'invoice_app/invoice_details.html'
