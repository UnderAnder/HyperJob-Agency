"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from main.views import MenuView, MyLoginView, SignupView, NewResumeView, NewVacancyView, HomeView
from resume.views import ResumesView
from vacancy.views import VacanciesView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', MyLoginView.as_view()),
    path('signup', SignupView.as_view()),
    path('home', RedirectView.as_view(url='home/')),
    path('home/', HomeView.as_view()),
    path('resume/new', NewResumeView.as_view()),
    path('vacancy/new', NewVacancyView.as_view()),
    path('resumes/', ResumesView.as_view()),
    path('vacancies/', VacanciesView.as_view()),
    path('', MenuView.as_view()),
]
