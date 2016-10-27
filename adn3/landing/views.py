from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from news.models import New


def index(request):
    if request.user.is_authenticated():
        return redirect('self:index')

    return render(request, 'landing/index.html', {
        'news': New.objects.all()[:5]
    })


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('self:index')
        else:
            return render(request, 'landing/signin.html')

    return redirect('landing:index')
