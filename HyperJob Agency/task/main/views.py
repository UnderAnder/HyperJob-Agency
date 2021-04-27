from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView

class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html')


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'signup.html'
