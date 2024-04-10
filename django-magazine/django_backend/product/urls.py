from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('catalog/<slug:category_slug>/<slug:catalog_slug>', views.product_page),
    path('catalog/', views.catalog_page),
    path('discount/', views.catalog_page_discount),
    path('catalog/<slug:catalog_slug>', views.catalog_page_product)
]
