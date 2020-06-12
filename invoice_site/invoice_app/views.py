from django.shortcuts import render, redirect
from .forms import InvoiceHomeForm, InvoiceInfoForm
from django.contrib import messages
from accounts.models import UserProfile
from .models import InvoiceHome, ItemInfo
from django.contrib.auth.models import User
from django.forms import inlineformset_factory


def dashboard_agent(request):
    if request.user.is_authenticated and UserProfile.objects.get(user=request.user).access_type == 'agent':

        if request.method == "POST":
            form = InvoiceHomeForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                # uploaded_file = request.FILES['document']

                # if uploaded_file.size <= 2097152 and uploaded_file.content_type == 'application/pdf':
                #     fs = uploaded_file.save()
                return redirect('details')
            else:
                messages.error(request, 'Size of the file must be <2mb and file should be a .pdf file')
                return redirect('dashboard_agent')
        else:
            form = InvoiceHomeForm()
        return render(request, 'invoice_app/invoice_page.html', {'form': form})
    elif request.user.is_authenticated and UserProfile.objects.get(user=request.user).access_type == 'manager':
        return redirect('dashboard_manager')
    else:
        return redirect('login')


def dashboard_manager(request):
    if request.user.is_authenticated and UserProfile.objects.get(user=request.user).access_type == 'manager':
        return render(request, 'invoice_app/manager_page.html')
    elif request.user.is_authenticated and UserProfile.objects.get(user=request.user).access_type == 'agent':
        return redirect('dashboard_agent')
    else:
        return redirect('login')


def dashboard_agent_details(request):

    if request.method == 'POST':
        form = InvoiceInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_details', user_id=request.user.id)

    form = InvoiceInfoForm()
    pdf = InvoiceHome.objects.filter(user_id=request.user.id).last()
    return render(request, 'invoice_app/invoice_details.html', {'form': form, 'pdf': pdf})


def dashboard_agent_item_details(request,user_id):
    user = User.objects.get(pk=user_id)
    ItemFormset = inlineformset_factory(User, ItemInfo, fields=('item_description', 'item_quantity', 'item_rate'),
                                        extra=1)

    if request.method == 'POST':
        formset = ItemFormset(request.POST, instance=user)
        if formset.is_valid():
            formset.save()
            return redirect('item_details', user_id=request.user.id)

    formset = ItemFormset(instance=user)
    pdf = InvoiceHome.objects.filter(user_id=request.user.id).last()
    return render(request, 'invoice_app/item_details.html', {'pdf': pdf, 'formset': formset})


def end_page(request):
    return render(request,'invoice_app/end.html')