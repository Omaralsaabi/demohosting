from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    html = "<html><body><h1>السلام عليكم</h1></body></html>"
    return HttpResponse(html)