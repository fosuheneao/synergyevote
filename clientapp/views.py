from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(f"<h1>{ request.tenant } home page</h1>")
