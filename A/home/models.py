from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True , blank=True)
    title = models.CharField(max_length=200, verbose_name='عنوان')
    secondTitle = models.CharField(max_length=200, verbose_name='عنوان دوم')
    slug = models.SlugField(max_length=500, unique=True, allow_unicode=True)
    bodySection1 = models.TextField(verbose_name='بخش اول محتوا')
    bodySection2 = models.TextField(verbose_name='بخش دوم محتوا')
    bodySection3 = models.TextField(verbose_name='بخش سه محتوا')
    bodySection4 = models.TextField(verbose_name='بخش چهارم محتوا')
    bodyPoint = models.TextField(max_length=400, verbose_name='نکته',)
    mainPoster = models.ImageField(upload_to='%Y/%m/%d' ,verbose_name='عکس اصلی')
    secondPoster = models.ImageField(upload_to='%Y/%m/%d' ,verbose_name='عکس دوم')
    thirdPoster = models.ImageField(upload_to='%Y/%m/%d' ,verbose_name='عکس سوم')
    postersTitle = models.CharField(max_length=100 ,verbose_name='عنوان عکس ها')
    is_published = models.BooleanField(default=False, verbose_name='منتشر شده')
    created = models.DateTimeField(auto_now=True ,verbose_name='تاریخ ساخت')
    updated = models.DateTimeField(auto_now_add=True ,verbose_name='تاریخ بروزرسانی')

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title, allow_unicode=True)
            slug = base_slug
            counter = 1
            while BlogPost.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
