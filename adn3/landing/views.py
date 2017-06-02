from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from adn3.services import is_teacher, is_student
from news.models import New


def index(request):
    if request.user.is_authenticated():
        if is_teacher(request.user):
            return redirect('self:index')
        elif is_student(request.user):
            return redirect('public:course_list')

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

            # redirect the user accordingly
            if is_teacher(user):
                return redirect('self:index')
            elif is_student(user):
                return redirect('public:course_list')
        else:
            return render(request, 'landing/signin.html')

    return redirect('landing:index')


def log_out(request):
    logout(request)
    return redirect('landing:index')
