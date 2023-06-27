from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('blog', views.blog, name='blog'),
    path('frequently_questions', views.frequently_questions, name='frequently_questions'),
]