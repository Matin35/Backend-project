from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . forms import UserRegistrationForm ,UserLoginForm
from django.views import View
from django.contrib import messages




class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                email=cd['email'],
                username=cd['username'],
            )
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.set_password(cd['password'])
            user.save()
            messages.success(request,'حساب شما با موفقیت ایجاد شد', 'success')
            return redirect('accounts:login')


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'شما با موفقیت وارد حساب خود شدید', 'success')
                return redirect('home:home')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'شما با موفقیت خارج شدید', 'success')
        return redirect('home:home')