from django.shortcuts import render
from .models import Human


def index(request):
    humans = Human.objects.all()
    return render(request, 'main/index.html', {'title': 'Main site page', 'humans': humans})


def about(request):
    return render(request, 'main/about.html')

