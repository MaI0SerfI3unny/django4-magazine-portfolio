from django.shortcuts import get_object_or_404
from .models import Articles
from django.shortcuts import render

def articles_page(request):
    article = Articles.objects.filter(is_published=1)
    return render(request, 'articles/index.html', {'articles': article})
def article_page(request, id):
    article = get_object_or_404(Articles, slug=id, is_published=1)
    return render(request, 'articles/page.html', {'article': article})