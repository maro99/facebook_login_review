from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def login(request):


    if request.method == 'POST':
        return render(request, 'main.html')

    else:
        return render(request,'members/login.html')

def facebook_login(request):
    # code = request.GET.get('code')
    # user = authenticate(request, code=code)
    #
    # if user is not None:
    #     login(request, user)
    #     return redirect('index')
    # return redirect('members:login')


    if request.method == 'POST':
        return render(request, 'facebook_login_succed.html')

    else:
        return render(request,'members/login.html')


def login_page(request):

    return render(request, 'members/login.html')