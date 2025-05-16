from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from . forms import BlogPostForm, BlogUpdateForm
from . models import BlogPost
from django.contrib import messages


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
        posts = BlogPost.objects.all()
        return render(request, 'home/blog.html', {'posts': posts})

class BlogCreateView(View):
    def get(self, request):
        form = BlogPostForm()
        return render(request, 'home/blog_create.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                blogPost = BlogPost.objects.create(
                    user=request.user,
                    title=cd['title'],
                    secondTitle=cd['secondTitle'],
                    bodySection1=cd['bodySection1'],
                    bodySection2=cd['bodySection2'],
                    bodySection3=cd['bodySection3'],
                    bodySection4=cd['bodySection4'],
                    bodyPoint=cd['bodyPoint'],
                    mainPoster=cd['mainPoster'],
                    secondPoster=cd['secondPoster'],
                    thirdPoster=cd['thirdPoster'],
                    postersTitle=cd['postersTitle'],
                )
                return redirect('home:blog_detail', blogPost.slug)
        else:
            messages.error(request, 'ابتدا وارد شوید.', 'danger')
            return redirect('account:login')
        messages.error(request, 'فیلد ها به درستی پر نشدند.', 'danger')
        return redirect('home:blog_create')


class BlogUpdateView(View):
    def get(self, request, Post_slug):
        post = BlogPost.objects.get(slug = Post_slug)
        form = BlogUpdateForm(instance=post)
        return render(request, 'home/blog_edit.html', {'form': form})

    def post(self, request, Post_slug):
        if request.user.is_authenticated:
            post = BlogPost.objects.get(slug=Post_slug)
            form = BlogUpdateForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'تغییر با موفقیت اعمال شد.', 'success')
                return redirect('home:blog_detail', Post_slug)
        else:
            messages.error(request, 'ابتدا وارد شوید.', 'danger')
            return redirect('home:login')



class BlogDeleteView(View):
    def get(self, request, Post_slug):
        if request.user.is_authenticated:
            post = BlogPost.objects.get(slug = Post_slug)
            post.delete()
            return redirect('home:blog')
        else:
            messages.error(request, 'ابتدا وارد شوید.', 'danger')
            return redirect('home:login')





class BlogDetailView(View):
    def get(self, request, Post_slug):
        post = get_object_or_404(BlogPost, slug=Post_slug)
        return render(request, 'home/blog_detail.html', {'post': post})



class ContactView(View):
    def get(self, request):
        return render(request, 'home/contact.html')