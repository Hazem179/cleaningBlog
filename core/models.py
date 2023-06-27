from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True,verbose_name="القسم")
    slug = models.SlugField(max_length=100, unique=True,verbose_name="الرابط")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "القسم"
        verbose_name_plural = "الأقسام"

class SubCategories(models.Model):
    name = models.CharField(max_length=100, unique=True,verbose_name="القسم الفرعي")
    slug = models.SlugField(max_length=100, unique=True,verbose_name="الرابط")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,verbose_name="القسم")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "القسم الفرعي"
        verbose_name_plural = "الأقسام الفرعية"

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True,verbose_name="عنوان الخدمة")
    slug = models.SlugField(max_length=100, unique=True,verbose_name="الرابط")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,verbose_name="القسم")
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE,verbose_name="القسم الفرعي")
    description = models.TextField(verbose_name="الوصف")
    image = models.ImageField(upload_to='post',verbose_name="الصورة")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "الخدمة"
        verbose_name_plural = "الخدمات"