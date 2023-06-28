from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('blog', views.blog, name='blog'),
    path('frequently_questions', views.frequently_questions, name='frequently_questions'),
    path('category/<str:slug>', views.category, name='category'),
    path('blog_post', views.blog_post, name='blog_post'),
]
