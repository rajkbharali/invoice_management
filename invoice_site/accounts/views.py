from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from .models import UserProfile, User
from .forms import RegisterForm, UserProfileForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        form1 = UserProfileForm(data=request.POST)

        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            user_type = form1.save(commit=False)
            user_type.user = user
            user_type.save()

            return redirect('login')

    else:
        form = RegisterForm()
        form1 = UserProfileForm()

    context = {'form': form, "form1": form1}
    return render(request, 'accounts/signup.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                type_obj = UserProfile.objects.get(user=user)
                if user.is_authenticated and type_obj.access_type == 'agent':
                    return redirect('dashboard_agent')
                elif user.is_authenticated and type_obj.access_type == 'manager':
                    return redirect('dashboard_manager')
        else:
            return redirect('login')

    return render(request, 'accounts/login.html')
