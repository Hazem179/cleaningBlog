import os
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True,verbose_name="القسم")
    description = models.TextField(verbose_name="الوصف")
    slug = models.SlugField(max_length=100,blank=True,verbose_name="الرابط")

    def save(self, *args, **kwargs):
        name = self.name
        self.slug = slugify(name, allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "القسم"
        verbose_name_plural = "الأقسام"

class SubCategories(models.Model):
    name = models.CharField(max_length=100, unique=True,verbose_name="القسم الفرعي")
    slug = models.SlugField(max_length=100, blank=True,verbose_name="الرابط")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,verbose_name="القسم")

    def save(self, *args, **kwargs):
        name = self.name
        self.slug = slugify(name, allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "القسم الفرعي"
        verbose_name_plural = "الأقسام الفرعية"

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True,verbose_name="عنوان الخدمة")
    slug = models.SlugField(max_length=100,blank=True,verbose_name="الرابط")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,verbose_name="القسم")
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE,verbose_name="القسم الفرعي")
    description = models.TextField(verbose_name="الوصف")
    image = models.ImageField(upload_to='post',verbose_name="الصورة")
    content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        title = self.title
        self.slug = slugify(title, allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "الخدمة"
        verbose_name_plural = "الخدمات"

class About(models.Model):
    phone_number = models.CharField(max_length=100,blank=True,null=True,verbose_name="رقم الهاتف")
    telephone = models.CharField(max_length=100,blank=True,null=True,verbose_name="التليفون")
    instagram_link = models.CharField(max_length=100,blank=True,null=True,verbose_name="رابط الانستغرام")
    facebook_link = models.CharField(max_length=100,blank=True,null=True, verbose_name="رابط الفيسبوك")
    twitter_link = models.CharField(max_length=100,blank=True,null=True, verbose_name="رابط التويتر")
    snapchat_link = models.CharField(max_length=100, blank=True,null=True,verbose_name="رابط السناب شات")
    email_link = models.CharField(max_length=100,blank=True,null=True, verbose_name="البريد الإلكتروني")
    state = models.BooleanField(default=True,verbose_name="فعالة")

    def __str__(self):
        return self.phone_number
    class Meta:
        verbose_name = "عن الشركة"
        verbose_name_plural = "عن الشركة"

class ServiceCities(models.Model):
    name = models.CharField(max_length=100, unique=True,verbose_name="المدينة")
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        name = self.name
        self.slug = slugify(name, allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "المدينة"
        verbose_name_plural = "المدن"


class FrequentlyQuestions(models.Model):
    title = models.CharField(max_length=200, unique=True,verbose_name="السؤال")
    content = models.TextField(verbose_name="الإجابة")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "الأسئلة الشائعة"
        verbose_name_plural = "الأسئلة الشائعة"

class CityPosts(models.Model):
    city = models.ForeignKey(ServiceCities, on_delete=models.CASCADE,verbose_name="المدينة")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,verbose_name="الخدمة")
    def __str__(self):
        return self.city.name
    class Meta:
        verbose_name = "الخدمة في المدينة"
        verbose_name_plural = "الخدمات في المدن"



def post_image_path(instance, filename):
    post_name = instance.post.title
    return os.path.join('post', post_name, filename)
class PostPictures(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=post_image_path)