from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views import View


class LoginView(View):
    
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('blog-list')
        else:
            messages.error(request, "Invalid username or password.")
        return render(request, 'login.html', {"form": form})


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('login')