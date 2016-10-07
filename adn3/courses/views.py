from django.shortcuts import render, get_object_or_404, redirect
from models import *


def show(request, pk):
    course = get_object_or_404(Course, pk=pk)

    return render(request, 'courses/show.html', {
        'course': course
    })


def index(request):
    return redirect('self:index')
