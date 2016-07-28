from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from common.models import UserProfile
from django.db import IntegrityError


def register(request):
    results = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            user = UserProfile.objects.create(username=username)
            user.set_password(password)
            user.save()
            return redirect('/login/')
        except IntegrityError:  # unique=True를 이용한 try ... except 코딩
            results['error'] = 'Already Used!'
    return render(request, 'register.html', results)


def login(request):
    results = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')  # username이 있으면 할당, 없으면 두 번째 인자값으로 할당
        password = request.POST.get('password', '')
        # 각각 username과 password를 찾아서 있으면 user객체를 반환, 없으면 null 반환
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)  # request와 user 객체를 넘겨줘서 실제 로그인을 시켜주는 메서드
            return redirect('/')
        else:
            results['error'] = 'Wrong! Try Again!'
    return render(request, 'login.html', results)


def logout(request):
    auth_logout(request)
    return redirect('/login/')


def index(request):
    return render(request, 'login.html')

