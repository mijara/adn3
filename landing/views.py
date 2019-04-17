from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from adn3.services import is_teacher, is_student, is_assistant, welcome_message


def index(request):
    if request.user.is_authenticated():
        if is_teacher(request.user) and is_student(request.user):
            return redirect('landing:choice')
        if is_teacher(request.user):
            return redirect('teachers:index')
        elif is_student(request.user):
            return redirect('students:agenda_list')

    return render(request, 'landing/index.html', {
        'welcome_message': welcome_message()
    })


def choice(request):
    if request.user.is_authenticated():
        if is_teacher(request.user) and is_student(request.user):
            return render(request, 'landing/choice.html', {
                'welcome_message': welcome_message()
            })

    return redirect('landing:index')


def sign_in(request, err_code=0):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            # redirect the user accordingly
            if is_teacher(request.user) and is_student(request.user):
                return redirect('landing:choice')
            elif is_teacher(user):
                return redirect('teachers:index')
            elif is_student(user):
                return redirect('students:agenda_list')
        else:
            return render(request, 'landing/signin.html', {
                'err_message': 'Credenciales inválidas, intente nuevamente.'
            })

    # translate error code.
    err_message = ''
    if err_code == '1':
        err_message = 'Usted ya tiene una cuenta en el sistema con este correo, ' \
                      'por favor inicie sesión para continuar.'

    return render(request, 'landing/signin.html', {
        'err_message': err_message
    })


def log_out(request):
    logout(request)
    return redirect('landing:index')
