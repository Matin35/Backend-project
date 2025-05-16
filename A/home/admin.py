from django.contrib import admin
from . models import BlogPost
from django.utils.html import format_html




class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'image_tag', 'created', 'is_published',)
    list_filter = ('is_published',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.mainPoster.url}" width="50px" height="50px" style="border-radius: 50%;" />')



admin.site.register(BlogPost, PostAdmin)