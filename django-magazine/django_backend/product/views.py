from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *

def index(request):
    data = {
        "title": "Product main page",
        "hover": "Main page product"
    }
    return render(request, 'product/page.html', data)

def catalog_page(request):
    get_category = Category.objects.all()
    data = {
        'categories': get_category
    }
    return render(request,'catalog/index.html',data)

def catalog_page_product(request,catalog_slug):
    get_category = get_object_or_404(Category, slug=catalog_slug)
    products = Product.objects.filter(cat_id=get_category.pk)
    for item in products:
        if item.discount > 0:
            discounted_price = item.price - ((item.price * item.discount) / 100)
            item.discounted_price = discounted_price

    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    num_pages = paginator.num_pages

    data = {
        'category': get_category,
        'products': page_obj,
        'num_pages': num_pages
    }
    return render(request,'catalog/page.html', data)

def catalog_page_discount(request):
    products = Product.objects.filter(is_published=True, discount__gt=0).select_related('cat').all()

    for item in products:
        if item.discount > 0:
            discounted_price = item.price - ((item.price * item.discount) / 100)
            item.discounted_price = discounted_price

    data = {
        'products': products
    }
    return render(request,'catalog/discount.html', data)

def product_list(request):
    products = Product.objects.filter(is_published=True).select_related('cat').all()
    for item in products:
        if item.discount > 0:
            discounted_price = item.price - ((item.price * item.discount) / 100)
            item.discounted_price = discounted_price

    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    num_pages = paginator.num_pages

    data = {
        'products': page_obj,
        'num_pages': num_pages
    }
    return render(request,'catalog/products.html', data)

def product_page(request, category_slug, catalog_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, slug=catalog_slug)
    if product.discount > 0:
        discounted_price = product.price - ((product.price * product.discount) / 100)
        product.discounted_price = discounted_price

    data = {
        'product': product,
        'category': category
    }
    return render(request,'catalog/single.html', data)