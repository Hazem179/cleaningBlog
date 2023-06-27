from django.shortcuts import render
from .models import ServiceCities,Post,FrequentlyQuestions
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
    print(context)
    return render(request, 'site/blog_page.html',context)


def frequently_questions(request):
    questions = FrequentlyQuestions.objects.all()
    context = {'questions': questions}
    context.update(categories_context())
    return render(request, 'site/frequentlyQuestions_page.html',context)


def category(request,slug):
    context = categories_context()
    return render(request, 'subPages/category.html',context)
