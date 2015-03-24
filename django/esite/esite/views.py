from django.http import HttpResponse
from django.shortcuts import render

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html', {'page_title': 'home'})