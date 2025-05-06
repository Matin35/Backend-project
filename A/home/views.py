from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home/landing.html')


class ResumeView(View):
    def get(self, request):
        return render(request, 'home/resume.html')


class WorksView(View):
    def get(self, request):
        return render(request, 'home/works.html')



class BlogView(View):
    def get(self, request):
        return render(request, 'home/blog.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'home/contact.html')



