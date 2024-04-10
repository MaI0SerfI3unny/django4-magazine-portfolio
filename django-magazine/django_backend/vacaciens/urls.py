from django.urls import path
from . import views

urlpatterns = [
    path('vacancy/', views.vacancy_page),
    path('vacancy/<int:id>', views.vacancy_single),
]
