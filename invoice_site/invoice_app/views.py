from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from invoice_app import forms
from django.views.generic import TemplateView,CreateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.

# def users(request):
#     form = InvoiceForm()


def dashboard(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        if uploaded_file.size <= 2097152 and uploaded_file.content_type == 'application/pdf':
            fs.save(uploaded_file.name,uploaded_file)
            return redirect('/dashboard/details')
        else:
            messages.error(request,'Size of the file must be <2mb and file should be a .pdf file')
            return redirect('/dashboard')
    return render(request,'invoice_app/invoice_page.html')


class DetailsPage(CreateView):
    form_class = forms.InvoiceForm
    template_name = 'invoice_app/invoice_details.html'
