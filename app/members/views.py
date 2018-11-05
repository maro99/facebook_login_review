from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import authenticate, login, logout, get_user_model


# Create your views here.
from config import settings


User = get_user_model()

def normal_login(request):


    if request.method == 'POST':
        return render(request, 'main.html')

    else:
        return render(request,'members/login.html')

def facebook_login(request):

    # access token 얻기

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






    # aceess token 검사 --> fb id등 정보 받기

    url = 'https://graph.facebook.com/debug_token'

    params = {
        'input_token':access_token,
        'access_token':'{}|{}'.format(
            settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET_CODE
        )
    }
    # response = requests.get(url, params)

    # 위에서 받은 response중 이름등 추가적 가져오기 위해서 scope를 전달해 줘야 한다. ----> http에 추가해 놓았다.






    # GraphAPI를 통햬써 Facebook User정보 받아오기.
    url = 'https://graph.facebook.com/v3.0/me'

    params = {
        'fields':
            ','.join(['id', 'name', 'first_name', 'last_name', 'picture']),
        'access_token': access_token,
    }
    response = requests.get(url, params)
    response_dict = response.json()









    # 받아온 정보 중 회원가입에 필요한 요소들 꺼내기
    facebook_user_id = response_dict['id']
    first_name = response_dict['first_name']
    last_name = response_dict['last_name']
    url_img_profile = response_dict['picture']['data']['url']

    # 있으면 get없으면 create하고 True도 같이 반환 .
    user, user_created = User.objects.get_or_create(
        username = facebook_user_id,
        defaults = {
            'first_name': first_name,
            'last_name': last_name,
        }
    )

    login(request, user)

    # return redirect('index')

    if user is not None:
        login(request, user)
        return render(request,'facebook_login_succed.html')

    return redirect('main')


def login_page(request):

    return render(request, 'members/login.html')