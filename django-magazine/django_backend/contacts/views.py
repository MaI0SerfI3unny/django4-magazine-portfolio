from django.shortcuts import render
from main.models import Map

def contact_page(request):
    map = Map.objects.filter(is_published=1)
    data = {
        "maps": map
    }
    return render(request, 'contact/index.html',data)
