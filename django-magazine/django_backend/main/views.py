from django.shortcuts import render
from articles.models import Articles
from product.models import Product
from .models import Map

def index(request):
    published_articles = Articles.objects.filter(is_published=1)[:3]
    map = Map.objects.filter(is_published=1)

    product_latest = Product.objects.filter(discount=0).order_by('-time_created').order_by('?')[:4].select_related('cat').all()
    product_discount = Product.objects.filter(discount__gt=0).order_by('-time_created').order_by('?')[:4]

    for product in product_discount:
        if product.discount > 0:
            discounted_price = product.price - ((product.price * product.discount) / 100)
            product.discounted_price = discounted_price

    data = {
        "title": "Северяночка - лучший магазин продуктов",
        "hover": "Main page product",
        "articles": published_articles,
        "maps": map,
        "product": product_latest,
        "discount": product_discount
    }
    return render(request, 'main/index.html', data)
