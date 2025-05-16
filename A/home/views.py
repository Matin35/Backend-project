from django.shortcuts import render, get_object_or_404
from django.views import View
from . models import Post


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
        posts = Post.objects.all()
        return render(request, 'home/blog.html', {'posts': posts})

class ContactView(View):
    def get(self, request):
        return render(request, 'home/contact.html')


class BlogDetailView(View):
    def get(self, request, Post_slug):
        post = get_object_or_404(Post, slug=Post_slug)
        return render(request, 'home/blog_detail.html', {'post': post})