from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from accounts import forms
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from .forms import UserProfileForm,RegisterForm

# Create your views here.

# class SignUp(CreateView):
#     form_class = forms.SignUpForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'


# class LogIn(TemplateView):
#     if request.method == 'POST':

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        form1 = UserProfileForm(response.POST)

        if form.is_valid() and form1.is_valid():
            user = form.save()

            user_type = form1.save(commit=False)
            user_type.user = user
            user_type.save()

            return redirect('/login')

    else:
        form = RegisterForm()
        form1 = UserProfileForm()

    context = {'form':form,"form1":form1}
    return render(response, 'accounts/signup.html',context)

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#
#             return redirect('/dashboard')
#         else:
#             form = AuthenticationForm()
#         return render(request,'registration/login.html',{'form':form})




