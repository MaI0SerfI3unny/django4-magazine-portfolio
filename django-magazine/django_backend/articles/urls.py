from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles_page),
    path('articles/<slug:id>', views.article_page),
]
