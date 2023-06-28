from django.shortcuts import render
from .models import ServiceCities, Post, FrequentlyQuestions, Categories
from .utils import categories_context


# Create your views here.

def home(request):
    questions = FrequentlyQuestions.objects.all()
    context = {'questions': questions}
    context.update(categories_context())
    return render(request, 'site/home_page.html', context)


def about(request):
    cities = ServiceCities.objects.all()
    context = {'cities':cities}
    context.update(categories_context())
    return render(request, 'site/about_page.html',context)


def services(request):
    context = categories_context()
    return render(request, 'site/services_page.html',context)

def blog(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    context.update(categories_context())
    return render(request, 'site/blog_page.html',context)


def frequently_questions(request):
    questions = FrequentlyQuestions.objects.all()
    context = {'questions': questions}
    context.update(categories_context())
    return render(request, 'site/frequentlyQuestions_page.html',context)


def category(request,slug):
    category = Categories.objects.get(slug=slug)
    posts = Post.objects.filter(category=category)
    context = {'category': category, 'posts': posts}
    context.update(categories_context())
    return render(request, 'site/category_page.html', context)

def blog_post(request):
    # category = Categories.objects.get(slug=slug)
    # post = Post.objects.filter(slug=slug)
    # context = {'category': category, 'post': post}
    context = {}
    context.update(categories_context())
    return render(request, 'subPages/blogDetails_page.html', context)