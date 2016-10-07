from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from courses.models import *


@login_required
def index(request):
    return render(request, 'self/teachers/index.html', {
        'courses': Course.objects.all()
    })
