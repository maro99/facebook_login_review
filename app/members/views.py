from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests

# Create your views here.
from config import settings


def login(request):


    if request.method == 'POST':
        return render(request, 'main.html')

    else:
        return render(request,'members/login.html')

def facebook_login(request):

    code = request.GET.get('code')
    url = 'https://graph.facebook.com/v3.0/oauth/access_token'

    params = {
        'client_id':settings.FACEBOOK_APP_ID,
        'redirect_uri':'http://localhost:8000/facebook_login/',
        'client_secret':settings.FACEBOOK_APP_SECRET_CODE,
        'code':code,
    }

    response = requests.get(url,params)
    response_dict = response.json()
    access_token = response_dict['access_token']
    return HttpResponse(access_token)


def login_page(request):

    return render(request, 'members/login.html')