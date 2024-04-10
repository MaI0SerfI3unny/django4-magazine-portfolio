from django.shortcuts import render
from product.models import Product

def create_search(request):
    data_search = request.GET.get('search')

    product = Product.objects.filter(is_published=True, title__contains=data_search).select_related('cat').all()


    for item in product:
        if item.discount > 0:
            discounted_price = item.price - ((item.price * item.discount) / 100)
            item.discounted_price = discounted_price
    print(product)
    return render(request,'search/index.html', { 'products': product })