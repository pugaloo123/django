from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - Home',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': True,
    }

    return render(request, 'main/index.html', context=context)


def about(request):
    return HttpResponse('About')
