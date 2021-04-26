from django.shortcuts import render
from django.views import View
from .models import Resume


class ResumesView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resumes.html', {'resumes': resumes})
