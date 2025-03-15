from urllib import request
from .models import Client

def get_client_hostname():
    return request.get_host().split(':')[0].lower()

def get_client(request):
    hostname = get_client_hostname(request)
    submain   = hostname.split('.')[0]
    return Client.objects.filter(submain = submain).first()