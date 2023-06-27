from django.shortcuts import render
from .models import Categories,SubCategories


# Create your views here.

def home(request):
    categories = Categories.objects.all()
    sub_categories = SubCategories.objects.all()
    context = {'categories': categories,'subcategories':sub_categories}
    return render(request, 'site/home_page.html', context)


def about(request):
    categories = Categories.objects.all()
    sub_categories = SubCategories.objects.all()
    context = {'categories': categories,'subcategories':sub_categories}
    return render(request, 'site/about_page.html',context)


def services(request):
    categories = Categories.objects.all()
    sub_categories = SubCategories.objects.all()
    context = {'categories': categories,'subcategories':sub_categories}
    return render(request, 'site/services_page.html',context)

def blog(request):
    categories = Categories.objects.all()
    sub_categories = SubCategories.objects.all()
    context = {'categories': categories,'subcategories':sub_categories}
    return render(request, 'site/blog_page.html',context)


def frequently_questions(request):
    categories = Categories.objects.all()
    sub_categories = SubCategories.objects.all()
    context = {'categories': categories,'subcategories':sub_categories}
    return render(request, 'site/frequentlyQuestions_page.html',context)