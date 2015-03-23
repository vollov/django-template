from django.http import HttpResponse
from django.shortcuts import render

def detail(request, page_slug):
    return render(request, 'page/'+ page_slug +'.html', {'page_title': translateTitle(page_slug)})

def translateTitle(page_slug):
    string_list = page_slug.split('-');
    return " ".join(string_list)
