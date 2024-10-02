from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(View):
    def get(self, request):
        # Empty form
        form = UserRegisterForm()
        return render(request, 'tracker/signup.html', {'form': form})
    
    def post(self, request):
        # Data bounded form
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('tracker')
        
        return render(request, 'tracker/signup.html', {'form': form})

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'tracker/dashboard.html')
