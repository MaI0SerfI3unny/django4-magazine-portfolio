from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")