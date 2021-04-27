from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from resume.models import Resume
from vacancy.models import Vacancy


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


class NewPostForm(forms.Form):
    description = forms.CharField(min_length=10, max_length=1024)


class NewResumeView(View):
    def post(self, request, *args, **kwargs):
        request_user = User.objects.filter(username=request.user.username).first()
        description = request.POST.get('description')
        Resume.objects.create(author=request_user, description=description)
        return redirect('/home')


class NewVacancyView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden(status=403)
        request_user = User.objects.filter(username=request.user.username).first()
        description = request.POST.get('description')
        Vacancy.objects.create(author=request_user, description=description)
        return redirect('/home')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        new_post_form = NewPostForm()
        return render(request, 'profile.html', {'form': new_post_form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden(status=403)
        request_user = User.objects.filter(username=request.user.username).first()
        if request_user.is_staff:
            return redirect('/vacancy/new')
        else:
            return redirect('/resume/new')
