from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('works/', views.WorksView.as_view(), name='works'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    re_path(r'blog/(?P<Post_slug>[^/]+)/?$', views.BlogDetailView.as_view(), name='blog_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

