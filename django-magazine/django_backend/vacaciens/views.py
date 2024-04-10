from django.shortcuts import render, get_object_or_404
from .models import Vacancy

def vacancy_page(request):
    vacancy = Vacancy.objects.filter(is_published=1)
    return render(request, 'vacancy/index.html', { "vacancy": vacancy })


def vacancy_single(request,id):
    vacancy_content = get_object_or_404(Vacancy, id=id , is_published=1)
    return render(request, 'vacancy/page.html', { "content" : vacancy_content })