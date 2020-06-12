from django.shortcuts import render, redirect
from .forms import InvoiceHomeForm,InvoiceInfoForm
from django.contrib import messages
from accounts.models import UserProfile
from .models import InvoiceHome, InvoiceInfo


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
        return render(request, 'invoice_app/invoice_page.html',{'form':form})
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
    else:
        form = InvoiceInfoForm()
        pdf = InvoiceHome.objects.filter(user_id=request.user.id).last()
    return render(request,'invoice_app/invoice_details.html',{'form':form,'pdf':pdf})

