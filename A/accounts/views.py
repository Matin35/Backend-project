from django.shortcuts import render
from django.contrib.auth.models import User
from . models import UserRegistrationForm
from django.views import View




class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username=cd['username'],
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                email=cd['email'],
            )
            user.set_password(cd['password'])
            user.save()
