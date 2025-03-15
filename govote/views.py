from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from .utilities import get_client
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Synergy Electronic Voting Platform (Synergy EVP)</h1>")


def client_index(request):
    client = get_client(request)
    return render(request, 'client/client.html', {'client':client}) 

# def our_team(request):
#     client = get_client(request)
    
#     return render(request, 'client/our_team.html', {'client':client})